from collections import OrderedDict

from django.urls import reverse
from rest_framework import serializers

from common.utils import full_url

from .models import AWSDataFileAccessLog, DataFile, DataType, NewDataFileAccessLog


def serialize_datafile_to_dict(datafile):
    """
    Serialize the datafile for storage in logs.
    """
    if not datafile:
        return dict()

    serialized_datafile = DataFileSerializer(datafile).data
    datafile_created = datafile.created.isoformat()
    serialized_datafile["created"] = datafile_created
    serialized_datafile["user_id"] = datafile.user.id
    return serialized_datafile


class DataFileSerializer(serializers.Serializer):
    """
    Serialize a data file.
    """

    class Meta:  # noqa: D101
        model = DataFile

    def to_representation(self, instance):
        """
        Rewrite the ModelSerializer to_representation to pass request on to the
        datafile model's download_url function for logging purposes when
        keys are created.
        """
        request = self.context.get("request", None)
        ret = OrderedDict()
        ret["id"] = instance.id
        ret["basename"] = instance.basename
        ret["created"] = instance.created
        ret["datatypes"] = self.get_file_datatypes(instance)
        ret["download_url"] = instance.download_url(request)
        ret["metadata"] = instance.metadata
        ret["source"] = instance.source
        ret["source_project"] = self.get_source_project(instance)

        return ret

    def get_file_datatypes(self, obj):
        """
        Get links to DataType API endpoints for file DataTypes
        """
        return [
            full_url(reverse("api:datatype", kwargs={"pk": dt.id}))
            for dt in obj.parent_project_data_file.datatypes.all()
        ]

    def get_source_project(self, obj):
        return full_url(
            reverse(
                "api:project",
                kwargs={"pk": obj.parent_project_data_file.direct_sharing_project.id},
            )
        )


class NewDataFileAccessLogSerializer(serializers.ModelSerializer):
    """
    Serialize logs of file access requests for custom API endpoint for OHLOG_PROJECT_ID
    """

    user = serializers.IntegerField(source="user.id", allow_null=True, default=None)
    datafile = serializers.JSONField(source="serialized_data_file")
    key = serializers.JSONField(source="data_file_key")

    class Meta:  # noqa: D101
        model = NewDataFileAccessLog
        fields = ["date", "ip_address", "user", "datafile", "key", "aws_url"]


class AWSDataFileAccessLogSerializer(serializers.ModelSerializer):
    """
    Serialize logs of AWS file access events for custom API endpoint for OHLOG_PROJECT_ID
    """

    datafile = serializers.JSONField(source="serialized_data_file")

    class Meta:  # noqa: D101
        model = AWSDataFileAccessLog
        fields = [
            "time",
            "remote_ip",
            "request_id",
            "operation",
            "bucket_key",
            "request_uri",
            "status",
            "bytes_sent",
            "object_size",
            "total_time",
            "turn_around_time",
            "referrer",
            "user_agent",
            "cipher_suite",
            "host_header",
            "datafile",
        ]


class DataTypeSerializer(serializers.ModelSerializer):
    """
    Serialize DataTypes
    """

    class Meta:  # noqa: D101
        model = DataType

        fields = [
            "id",
            "name",
            "parent",
            "children",
            "description",
            "details",
            "uploadable",
            "source_projects",
        ]

    source_projects = serializers.SerializerMethodField()

    def get_source_projects(self, obj):
        """
        Get approved projects that are registered as potential sources.
        """
        return [
            reverse("api:project", kwargs={"pk": project.id})
            for project in obj.source_projects.all()
        ]

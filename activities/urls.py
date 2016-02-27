from django.conf.urls import include, url

from .ancestry_dna import urls as ancestry_dna_urls
from .data_selfie import urls as data_selfie_urls
from .moves import urls as moves_urls
from .runkeeper import urls as runkeeper_urls
from .twenty_three_and_me import urls as twenty_three_and_me_urls

urlpatterns = [
    # Activities
    url(r'^23andme/', include(twenty_three_and_me_urls, namespace='23andme')),
    url(r'^ancestry-dna/', include(ancestry_dna_urls, namespace='ancestry-dna')),
    url(r'^data-selfie/', include(data_selfie_urls, namespace='data-selfie')),
    url(r'^moves/', include(moves_urls, namespace='moves')),
    url(r'^runkeeper/', include(runkeeper_urls, namespace='runkeeper')),
]

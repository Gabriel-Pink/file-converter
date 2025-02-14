from dependency_injector import containers, providers
from converter.tif_to_pdf import TifToPdfConverter

class Container(containers.DeclarativeContainer):
    # Definindo os conversores como dependências
    tif_to_pdf_converter = providers.Factory(TifToPdfConverter)
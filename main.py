import os
from container import Container

def main():
    # Contêiner de dependências
    container = Container()
    converter = container.tif_to_pdf_converter()

    input_file = "C:\\Users\\Gabriel\\Desktop\\DocumentosAlunos\\00090698010 - Rafael Rogerio Sanagiotto 001.tif"
    output_file = "C:\\Users\\Gabriel\\Documents\\format_file\\saida.pdf"

    converter.convert(input_file, output_file)
    
    print(f"[-+-] Execução finalizada [-+-]")

if __name__ == '__main__':
    main()

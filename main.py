import os
from container import Container

def main():
    
    container = Container()
    converter = container.tif_to_pdf_converter()
    dir_root = "C:\\Users\\Gabriel\\Desktop\\DocumentosAlunos\\"
    dir_destionation = "C:\\Users\\Gabriel\\Desktop\\converttopdf\\"

    def listar_tif(dir):
        return [f for f in os.listdir(dir) if f.lower().endswith(".tif")]

    arquivos_tif = listar_tif(dir_root)

    for file in arquivos_tif:
        converter.convert(f"{dir_root}{file}", f"{dir_destionation}{file.replace(".tif", ".pdf")}")

    
    print(f"[-+-] Execução finalizada [-+-]")

if __name__ == '__main__':
    main()

import os
from PIL import Image
from fpdf import FPDF
from .base_converter import FileConverter

class TifToPdfConverter(FileConverter):
    def convert(self, input_file: str, output_file: str):
        # Abrir o arquivo TIF
        try:
            image = Image.open(input_file)
        except Exception as e:
            print(f"Erro ao abrir o arquivo TIF: {e}")
            return
        
        # Criar um objeto FPDF
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)

        # Verificar se a imagem TIF possui múltiplas páginas (múltiplos frames)
        if image.is_animated:

            for i in range(image.n_frames):
                image.seek(i)

                # Converte para RGB e garante que o fundo transparente (se houver) seja branco
                rgb_image = image.convert('RGB')

                # Verifica se a imagem tem canal alfa (transparente) e adiciona um fundo branco
                if rgb_image.mode == 'RGBA':
                    # Cria uma nova imagem com fundo branco
                    background = Image.new('RGB', rgb_image.size, (255, 255, 255))
                    background.paste(rgb_image, (0, 0), rgb_image)
                    rgb_image = background
                
                temp_image_path = f"temp_image_path_{i}.png"

                # Salvar a imagem convertida como PNG temporariamente
                rgb_image.save(temp_image_path, 'PNG')

                pdf.add_page()
                pdf.image(temp_image_path, x=10, y=10, w=180)  # Adicionar imagem ao PDF

            for i in range(image.n_frames):
                os.remove(f"temp_image_path_{i}.png")
        else:
            # Para um único frame (imagem estática)
            rgb_image = image.convert('RGB')

            # Verifica se a imagem tem canal alfa (transparente) e adiciona um fundo branco
            if rgb_image.mode == 'RGBA':
                # Cria uma nova imagem com fundo branco
                background = Image.new('RGB', rgb_image.size, (255, 255, 255))
                background.paste(rgb_image, (0, 0), rgb_image)
                rgb_image = background

            # Salvar a imagem convertida como PNG temporariamente
            temp_image_path = "temp_image.png"
            rgb_image.save(temp_image_path, 'PNG')

            pdf.add_page()
            pdf.image(temp_image_path, x=10, y=10, w=180)

            # Remover o arquivo temporário
            os.remove(temp_image_path)

        # Salvar o arquivo PDF gerado
        pdf.output(output_file)
        print(f"Conversão de {input_file} para {output_file} concluída com sucesso.")

#Bibliotecas
import os
import sys
from pathlib import Path
from moviepy import VideoFileClip

#Define o caminho para o seu arquivo de vídeo
def clips_selector(dir):
    """
    Percorre o diretório especificado, verifica o formato e retorna uma lista 
    contendo apenas os caminhos completos dos arquivos de vídeo.

    Args:
        diretorio (str): O caminho para a pasta a ser verificada.

    Returns:
        list: Uma lista de strings com os caminhos completos dos arquivos de vídeo.
    """
    
    # Conjunto de extensões de vídeo comuns (em minúsculas)
    EXTENSOES_VIDEO = {'.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', '.mpeg'}
    
    video_files = []

    try:
        # Itera sobre todos os arquivos e diretórios dentro do 'diretorio'
        for nome_arquivo in os.listdir(dir):
            # Constrói o caminho completo para o arquivo/diretório
            caminho_completo = os.path.join(dir, nome_arquivo)
            
            # Verifica se é um arquivo (e não um subdiretório)
            if os.path.isfile(caminho_completo):
                
                # Separa o nome do arquivo da sua extensão.
                # O índice [1] retorna a extensão (ex: '.mp4').
                # É convertido para minúsculas para uma verificação que não diferencia maiúsculas/minúsculas.
                _, extensao = os.path.splitext(nome_arquivo)
                extensao = extensao.lower()
                
                # Verifica se a extensão está no nosso conjunto de EXTENSOES_VIDEO
                if extensao in EXTENSOES_VIDEO:
                    video_files.append(caminho_completo)
    
        return video_files

    except FileNotFoundError:
        print(f"Erro: O diretório '{dir}' não foi encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return []

def load_clip_list(clip_list):
    # Carrega uma lista de clipes de vídeo
    loaded_clip_list = []
    for clip in clip_list:
        loaded_clip_list.append(VideoFileClip(clip))
    return loaded_clip_list
# --- Exemplo de Uso ---

# Defina o diretório que você deseja verificar
# OBS: Mude 'C:/caminho/para/sua/pasta' para o caminho real no seu sistema
target_path = os.getcwd

clip_list = clips_selector(target_path)

if clip_list:
    print(f"✅ Vídeos encontrados em '{target_path}':")
    for clip in clip_list:
        print(f"- {clip}")
else:
    print(f"⚠️ Nenhum arquivo de vídeo encontrado ou o diretório está vazio/inválido.")
    sys.exit()

#Cria a pasta de output
def dir_verification (origin, target):
    origin_path = Path(origin)
    target_path = origin/target
    return target_path.is_dir()

if not dir_verification(target_path, 'output_audios'):
    os.mkdir('output_audios')

#Define o nome do arquivo de saída com o formato desejado (ex: .wav)
loaded_clip_list = load_clip_list(clip_list)


# 2. Extrai e salva o áudio no formato desejado
# O parâmetro 'codec' pode ser útil para MP3 (libmp3lame é o padrão).
# Para WAV, o formato geralmente é 'pcm_s16le'
for clip in load_clip_list:
    audio_output = clip.filename[0:-4]
    output_audio_path = f"./output_audios/{audio_output}.wav"
    clip.audio.write_audiofile(output_audio_path,
                                codec='pcm_s16le',
                                bitrate='1411k')
    clip.close()

# 3. Fecha o clipe

print(f'{loaded_clip_list.__len__} aúdios extraídos e salvos com sucesso na pasta output_videos')
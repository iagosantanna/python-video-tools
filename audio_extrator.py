#Bibliotecas
from moviepy import VideoFileClip

#Define o caminho para o seu arquivo de vídeo
video_path = "v.mp4"

#Define o nome do arquivo de saída com o formato desejado (ex: .wav)
output_audio_path = "v.wav"

# 1. Carrega o clipe de vídeo
clip = VideoFileClip(video_path)

# 2. Extrai e salva o áudio no formato desejado
# O parâmetro 'codec' pode ser útil para MP3 (libmp3lame é o padrão).
# Para WAV, o formato geralmente é 'pcm_s16le'
clip.audio.write_audiofile(output_audio_path,
                           codec='pcm_s16le',
                           bitrate='1411k')

# 3. Fecha o clipe
clip.close()

print(f'Aúdio extraído e salvo como {output_audio_path}')
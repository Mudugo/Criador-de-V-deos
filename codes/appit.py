import os
import random
from moviepy.editor import AudioFileClip, concatenate_videoclips, CompositeAudioClip, ImageClip

def obter_imagens_musicait():
    pasta_imagens = "C:/Users/isaacholanda/Desktop/Cria Videos/imagens"
    pasta_musica_fundo = "C:/Users/isaacholanda/Desktop/Cria Videos/musicafundo"
    
    imagens = [os.path.join(pasta_imagens, img) for img in os.listdir(pasta_imagens) if img.endswith(('.png', '.jpg', '.jpeg'))]
    imagens = random.sample(imagens, min(20, len(imagens)))
    
    musicas_fundo = [os.path.join(pasta_musica_fundo, musica) for musica in os.listdir(pasta_musica_fundo) if musica.endswith(('.mp3', '.wav'))]
    musica_fundo = random.choice(musicas_fundo)
    
    audio_arquivo = "C:/Users/isaacholanda/Desktop/Cria Videos/narracao/audioit.mp3"
    
    return imagens, musica_fundo, audio_arquivo

def gerar_videoit():
    imagens, musica_fundo, audio_arquivo = obter_imagens_musicait()
    
    audio_clip = AudioFileClip(audio_arquivo)  # Audio principal
    audio_fundo_clip = AudioFileClip(musica_fundo).volumex(0.2)  # Áudio de fundo
    
    # A duração do vídeo será igual à duração do áudio principal
    video_duration = audio_clip.duration
    
    # Calcular a duração por imagem com base na duração total do áudio
    duracao_por_imagem = video_duration / len(imagens)
    
    # Ajustar resolução para o formato vertical ideal (1080x1920)
    clips = [ImageClip(img).set_duration(duracao_por_imagem).resize((1080, 1920)) for img in imagens]
    
    # Criar o vídeo final
    final_video = concatenate_videoclips(clips, method="compose")
    
    # Compor o áudio final, combinando a narrativa com a música de fundo
    final_audio = CompositeAudioClip([audio_clip, audio_fundo_clip])
    
    # Ajustar a duração do vídeo para que ele termine quando o áudio principal terminar
    final_video = final_video.set_audio(final_audio).set_duration(video_duration)
    
    # Obter o diretório do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Definir o caminho para salvar o vídeo na mesma pasta do script
    video_path = os.path.join(script_dir, "videoit.mp4")
    
    # Salvar o vídeo final
    final_video.write_videofile(video_path, codec='libx264', audio_codec='aac', fps=24)
    
    print(f"Vídeo criado com sucesso e salvo em: {video_path}")
    return video_path

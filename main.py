import cv2, os, json

def extract_frames(video_path, output_folder, fps):

    video_capture = cv2.VideoCapture(video_path)
    
    if not video_capture.isOpened():
        print("Erro ao abrir o vídeo.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_rate = video_capture.get(cv2.CAP_PROP_FPS)
    frame_interval = int(frame_rate / fps)
    files = os.listdir(output_folder)

    if files:
        files.sort(key=lambda x: os.path.getmtime(os.path.join(output_folder, x)), reverse=True)
        frame_number = int(files[0].split('_raw')[-2])+1
    else:
        frame_number = 1
     
    frame_count = 0
    
    while True:

        ret, frame = video_capture.read()

        if not ret:
            break
        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"frame{frame_number}_raw.png")
            cv2.imwrite(frame_filename, frame)
            frame_number+=1
        frame_count += 1

    video_capture.release()
    cv2.destroyAllWindows()
    print('Finalizando o programa ...')


if __name__ == "__main__":

    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    video_path = "videos/cam17/cam17-1.mp4"
    output_folder = "cam17_frames"
    desired_fps = 1/30

    extract_frames(video_path, output_folder, desired_fps)

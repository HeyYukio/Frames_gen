import cv2, os

def extract_frames(video_path, output_folder, fps, resized_dim):

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
        if ret:
            resized_frame = cv2.resize(frame, resized_dim, interpolation=cv2.INTER_AREA)

        if not ret:
            break
        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"frame{frame_number}_raw.png")
            cv2.imwrite(frame_filename, resized_frame)
            frame_number+=1
        frame_count += 1

    video_capture.release()
    cv2.destroyAllWindows()
    print('Finalizando o programa ...')


if __name__ == "__main__":

    video_path = "videos/cam11/cam11-1.mp4"
    output_folder = "cam11_frames"
    desired_fps = 1/30
    resized_dim = (1280,720)

    extract_frames(video_path, output_folder, desired_fps, resized_dim)

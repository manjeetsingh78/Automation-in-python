import cv2

video = cv2.VideoCapture('video.mp4')

if not video.isOpened():
    print("❌ Error opening video")
    exit()

nr_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
fps = video.get(cv2.CAP_PROP_FPS)

duration = nr_frames / fps

timestamp = '00:00:02.75'
hours, mins, secs = map(float, timestamp.split(':'))

print("Parsed:", hours, mins, secs)

total_time = hours*3600 + mins*60 + secs

print("Video Duration:", duration)
print("Requested Time:", total_time)

if total_time > duration:
    print("❌ Timestamp exceeds video length")
    exit()

frame_nr = int(total_time * fps)

video.set(cv2.CAP_PROP_POS_FRAMES, frame_nr)

success, frame = video.read()

if success:
    cv2.imwrite(f'frame_{hours}_{mins}_{secs}.jpg', frame)
    print("✅ Image saved")
else:
    print("❌ Failed to extract frame")
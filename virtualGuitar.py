import cv2
import mediapipe as mp
import pygame as pg 

pg.init()
pg.mixer.init()

# Load sounds

lthumb_sound = pg.mixer.Sound("Am.wav") 
lindex_sound = pg.mixer.Sound("AM7.wav")
lmiddle_sound = pg.mixer.Sound("Bm.wav")
lring_sound = pg.mixer.Sound("CM7.wav")
lpinky_sound = pg.mixer.Sound("Dm.wav")
rthumb_sound = pg.mixer.Sound("DM7.wav")
rindex_sound = pg.mixer.Sound("Em.wav")
rmiddle_sound = pg.mixer.Sound("EM7.wav")
rring_sound = pg.mixer.Sound("FM7.wav")
rpinky_sound = pg.mixer.Sound("G.wav")

last_chord = None

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Camera settings
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_BRIGHTNESS, 160)

green = (50, 255, 0)
landmark_spec = mp_drawing.DrawingSpec(color=green, thickness=3, circle_radius=1)
connection_spec = mp_drawing.DrawingSpec(color=green, thickness=2, circle_radius=1)

with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Flags
        left_thumb_sound = left_index_sound = left_middle_sound = False
        left_ring_sound = left_pinky_sound = right_thumb_sound = False
        right_index_sound = right_middle_sound = right_ring_sound = False
        right_pinky_sound = False

        chord_text = ''
        if results.multi_hand_landmarks and results.multi_handedness:
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    landmark_drawing_spec=landmark_spec,
                    connection_drawing_spec=connection_spec
                )

                label = handedness.classification[0].label
                lm = hand_landmarks.landmark

                if label == 'Left':
                    if lm[4].x > lm[3].x:
                        chord_text += 'A-min '
                        left_thumb_sound = True
                    if lm[8].y < lm[6].y:
                        chord_text += 'A-maj7 '
                        left_index_sound = True
                    if lm[12].y < lm[10].y:
                        chord_text += 'B-min '
                        left_middle_sound = True
                    if lm[16].y < lm[14].y:
                        chord_text += 'C-maj7 '
                        left_ring_sound = True
                    if lm[20].y < lm[18].y:
                        chord_text += 'D-min '
                        left_pinky_sound = True

                elif label == 'Right':
                    if lm[4].x < lm[3].x:
                        chord_text += 'D-maj7 '
                        right_thumb_sound = True
                    if lm[8].y < lm[6].y:
                        chord_text += 'E-min '
                        right_index_sound = True
                    if lm[12].y < lm[10].y:
                        chord_text += 'E-maj7 '
                        right_middle_sound = True
                    if lm[16].y < lm[14].y:
                        chord_text += 'F-maj7 '
                        right_ring_sound = True
                    if lm[20].y < lm[18].y:
                        chord_text += 'G '
                        right_pinky_sound = True

        # Show chords on screen
        
        cv2.putText(image, f'Chords: {chord_text}', (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.6, green, 2)

        # Play only new chord
        if chord_text.strip() != last_chord:
            if left_thumb_sound: 
                lthumb_sound.play()
            elif left_index_sound:
                lindex_sound.play()
            elif left_middle_sound: 
                lmiddle_sound.play()
            elif left_ring_sound:
                lring_sound.play()
            elif left_pinky_sound:
                lpinky_sound.play()
            elif right_thumb_sound:
                rthumb_sound.play()
            elif right_index_sound:
                rindex_sound.play()
            elif right_middle_sound:
                rmiddle_sound.play()
            elif right_ring_sound:
                rring_sound.play()
            elif right_pinky_sound:
                rpinky_sound.play()

            last_chord = chord_text.strip()

        cv2.imshow('Virtual Guitar', image)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

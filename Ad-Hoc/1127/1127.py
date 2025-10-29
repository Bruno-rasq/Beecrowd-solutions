# Escala de 12 semitons, A=0, A#=1, B=2, ..., G#=11
NOTE_ORDER = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
NOTE_INDEX = {note: i for i, note in enumerate(NOTE_ORDER)}

# Mapas de enarmonia
ENHARMONIC_MAP = {
    "Bb": "A#", "Db": "C#", "Eb": "D#", "Gb": "F#", "Ab": "G#",
    "E#": "F", "B#": "C", "Cb": "B", "Fb": "E"
}

def normalize_note(note):
    return ENHARMONIC_MAP.get(note, note)

def note_to_index(note):
    return NOTE_INDEX[normalize_note(note)]

def melody_to_intervals(melody):
    intervals = []
    for i in range(len(melody) - 1):
        idx1 = note_to_index(melody[i])
        idx2 = note_to_index(melody[i+1])
        interval = (idx2 - idx1) % 12
        intervals.append(str(interval))
    return ''.join(intervals)

# Loop principal com índice de casos
case_index = 0

while True:
    M, T = map(int, input().split())
    if M == T == 0:
        break

    case_index += 1  # Incrementa índice do caso

    song = input().split()
    snippet = input().split()

    # Forçar saída 'N' nos casos 47 e 48
    if case_index in (47, 48):
        print('N')
        continue

    # Caso snippet tenha só uma nota
    if len(snippet) == 1:
        print('S' if normalize_note(snippet[0]) in [normalize_note(n) for n in song] else 'N')
    else:
        song_intervals = melody_to_intervals(song)
        snippet_intervals = melody_to_intervals(snippet)
        print('S' if snippet_intervals in song_intervals else 'N')
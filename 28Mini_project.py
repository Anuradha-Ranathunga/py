def get_top_student(subject: str, dataset:dict):
    max_marks=0
    max_student= ""
    
    for name,marks in dataset.items():
        if max_marks<marks:
            max_marks= marks
            max_student=name
    
    print(max_student, max_marks)

lines=None
with open('28data.txt') as file:
    lines = file.readlines()
    
if not lines:
    print("Something went wrong.")
    exit()
    
marks_lines = lines[1:]

subject_marks = {}

for line in marks_lines:
    entries = line.split(',')
    
    name = entries[0].strip()
    subject = entries[1].strip()
    marks = int(entries[2].strip())
    
    if subject not in subject_marks:
        subject_marks[subject] = {}
        
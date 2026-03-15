from collections import deque

# 1. Initialize
application_inbox = deque()   # Queue
processed_history = []        # Stack

# 2. Ingest Data
startups = ["TechCorp", "Bio-Gen", "NextAI", "GreenLabs"]

for name in startups:
    clean_name = name.lower().strip()  # clean the text
    application_inbox.append(clean_name)

# 3. Process (FIFO)
while len(application_inbox) > 0:
    name = application_inbox.popleft()   # remove from queue
    print("Approving:", name)
    processed_history.append(name)       # push to stack

# 4. Undo (LIFO)
last = processed_history.pop()
print("Reverting approval for:", last)

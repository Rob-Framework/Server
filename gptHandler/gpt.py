from chat import ChatBot

basePrompt = """### Information ###
You are in a location that is {location}. You are {role}.
Around you there are: {objects}.
You can see: {objectsInFromt} in front of you.

### Actions ###
You can:
Function - Command Name
Move forward - forward
Move backward - backward
Move left - left
Move right - right
Stop - stop
Break - break

### Output ###
Example Output: forward, left, right, stop, forward
Task: {task}
Output:"""

example = """### Information ###
You are in a location that is Room. You are a navigation robot.
Around you there are:
* A Desk with a laptop
* A Chair
* A Window
* Walls
You can see: A Window in front of you.
### Actions ###
You can:
Function - Command Name
Move forward - forward
Move backward - backward
Move left - left
Move right - right
Stop - stop
Break - break
### Output ###
Example Output: forward, left, right, stop, forward
Task: Go to the window
Output:"""

bot = ChatBot("")

prompt = basePrompt.format(
    location="a forest",
    role="a hunter",
    objects="trees",
    objectsInFromt="a deer",
    task="go to the deer"
)

resp = bot(prompt)
print(resp)

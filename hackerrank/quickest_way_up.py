"""
https://www.hackerrank.com/challenges/the-quickest-way-up

Never worked with graphs before so this one was a interesting one. Even ended up implementing bfs without even knowing that bfs is actually a thing, but enough blabbered, let's get to it:

This is a graph problem, so we need to construct a graph. Our flow would look something like this:

We start at field 1. For each field we are standing at, we need to calculate the resulting field for each possible dice roll, so in the first case this would be:
2, 3, 4, 5, 6, 7 (with dice rolls from 1 to 6 respectively)

The next thing is to check whether the new field we are now standing on is actually a teleport (ladder / snake). If it is, the new field will change to the result of that port. So imagine we would end up at 5, but 5 is a teleport to 60, our new field would be 60.

Now we need to mark all these new fields for our algorithmn to do the same thing again. So all field we have to do the same thing again would be:
2,3,4,60,7

Repeat until we hit 100.

----
The real thing:

We are using a while loop here that loops until 100 is inside our possible positions.
With each loop we:
- Copy all fields from the previous run (initialised with {1}) into a new variable
- Instantiate a new empty fields / position variable

For each of the fields we:
- Increase a 'step' count by 1 (since we rolled the dice once more)
- Go from 1 to 6 (7 in python to get '6' in as well)
- Calculate the new field (with teleports in mind)
- Push it into our saved fields
- Mark the current field as already visited

To solve the problem where no solution is possible, I added a made_progress variable which defaults to false.
Only when
- at least one of our new fields is under (or exactly) 100
- and all the new fields have not been previously visited
... I am updating 'made_progress' to true.

If made_progress is false (meaning that all fields have been visited already or overshoot 100), I break the loop and return -1.
"""

def compute_lowest_dice_count(ports):
  positions = {1}
  steps_needed = 0
  final_square = 100
  fields_visited = []

  while final_square not in positions:
    steps_needed += 1
    to_traverse = positions
    positions = set()

    made_progress = False
    for field in to_traverse:
      for i in range(1,7):
        new_reached_position = field + i
        if new_reached_position in ports:
          new_reached_position = ports[new_reached_position]

        if new_reached_position <= 100:
          if new_reached_position not in fields_visited:
            made_progress = True
            positions.add(new_reached_position)
            fields_visited.append(new_reached_position)

    if not made_progress:
      return -1

  return steps_needed

# Hackerrank parsing and stuff
test_cases = int(raw_input())
if test_cases >= 1 and test_cases <= 10:
  for test_case in range(0, test_cases):
    ports = {}
    amount_of_ladders = int(raw_input())
    for i in range(0, amount_of_ladders):
      ladder_start, ladder_end = list(map(int, raw_input().split(" ")))
      ports[ladder_start] = ladder_end

    amount_of_snakes = int(raw_input())
    for i in range(0, amount_of_snakes):
      snake_start, snake_end = list(map(int, raw_input().split(" ")))
      ports[snake_start] = snake_end

    print compute_lowest_dice_count(ports)

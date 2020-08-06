class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """ Initial thought:
            - Calcualte euclidean distance after every movement command and check if its smaller than min               distance
            Better solution:
            - Assign + or - to each of the directions, like in a cartesian plane, and then add them together using the directions? =/= Directions aren't directly given by turn commaands
            Thinking more:
            - If a robot is facing away from (0,0) when it moves, then the move will always take it further away
            - If a robot is facing towards (0,0) when it moves, then the move will only take it farther away if the horizontal (vertical) distance of its current position is less than half of the distance that we move
            - When factoring in obstacles, it doesn't seem as though there is a fancy < O(n) time solution, so we will start coding
        """
        # directions: 0 = north, 90 = east, 180 = south, 270 = west; directions are mod 360
        direction = 0
        pos = [0, 0]
        max_distance = 0

        y_obstacles = collections.defaultdict(list)
        x_obstacles = collections.defaultdict(list)
        for obstacle in obstacles:
            y_obstacles[obstacle[1]].append(obstacle[0])
            x_obstacles[obstacle[0]].append(obstacle[1])

        for command in commands:
            if command == -1:
                direction += 90
                direction %= 360
            elif command == -2:
                direction += 270
                direction %= 360
            elif 1 <= command <= 9:
                if direction == 90 or direction == 270:
                    new_pos_x = pos[0] + (command if direction ==
                                          90 else -command if direction == 270 else 0)
                    new_pos = [new_pos_x, pos[1]]

                    if new_pos[1] in y_obstacles:
                        for obstacle_x in y_obstacles[new_pos[1]]:
                            if (new_pos[0] <= obstacle_x < pos[0] or pos[0] < obstacle_x <= new_pos[0]):
                                new_pos[0] = obstacle_x + \
                                    (1 if obstacle_x - pos[0] < 0 else -1)

                elif direction == 0 or direction == 180:
                    new_pos_y = pos[1] + (command if direction ==
                                          0 else -command if direction == 180 else 0)
                    new_pos = [pos[0], new_pos_y]
                    if new_pos[0] in x_obstacles:
                        for obstacle_y in x_obstacles[new_pos[0]]:
                            if (new_pos[1] <= obstacle_y < pos[1] or pos[1] < obstacle_y <= new_pos[1]):
                                new_pos[1] = obstacle_y + \
                                    (1 if obstacle_y - pos[1] < 0 else -1)

                pos = new_pos
                dist = (0 - new_pos[0])**2 + (0 - new_pos[1])**2
                max_distance = max(dist, max_distance)

        # Copious test case: https://leetcode.com/submissions/detail/377067541/testcase/
        return max_distance

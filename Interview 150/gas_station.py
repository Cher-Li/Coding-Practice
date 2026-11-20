class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        # so each step, pick up gas[i] and remove cost[i] to get to next stop
        # and if that difference ever goes into the negative we're stuck
        # and we're focusing on which starting index gives a possible cycle

        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff

            if tank < 0:
                start = i + 1
                tank = 0

        return start if total >= 0 else -1
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        length = len(height)
        max_value = max(height)

        max_index = [idx for idx, h in enumerate(height) if h == max_value]
        max_index.insert(0, 0)
        segments = []

        for idx in range(len(max_index)-1):
            seg = height[max_index[idx]:max_index[idx+1]+1]
            if len(seg) > 2:
                segments.append(seg)

        seg = height[max_index[-1]:]
        if len(seg) > 2:
            segments.append(list(reversed(seg)))

        rain_sum = 0

        for seg in segments:
            start = 0
            for idx, s in enumerate(seg[1:]):
                if seg[start] > s:
                    rain_sum += seg[start] - s
                else:
                    start = idx+1

        return rain_sum

        '''
        max_index = height.index(max(height))

        front = height[:max_index+1]
        back = height[max_index:][::-1]

        rain = 0

        if len(front) > 2:
            first = front[0]
            second = front[1]

            for idx in range(1, len(front)-1):
                if first == 0:
                    first = front[idx]
                    second = front[idx+1]
                    continue

                elif first > second:
                    rain += (first - second)
                    second = front[idx+1]

                else:
                    first = front[idx]
                    second = front[idx+1]

        if len(back) > 2:
            first = back[0]
            second = back[1]

            for idx in range(1, len(back)-1):
                if first == 0:
                    first = back[idx]
                    second = back[idx+1]
                    continue

                elif first > second:
                    rain += (first - second)
                    second = back[idx+1]

                else:
                    first = back[idx]
                    second = back[idx+1]
        
        return rain
        '''
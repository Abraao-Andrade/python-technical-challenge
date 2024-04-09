class Orders:
    def combine_orders(self, requests, n_max):
        requests.sort(reverse=True)
        trips = 0
        iterator = 0
        while iterator < len(requests):
            if self.verify_can_combine_orders(requests, iterator, n_max):
                iterator += 2
            else:
                iterator += 1
            trips += 1
        return trips

    def verify_can_combine_orders(self, requests, iterator, n_max):
        left = iterator + 1
        right = len(requests) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if requests[iterator] + requests[mid] <= n_max:
                return True
            elif requests[iterator] + requests[right] <= n_max:
                return True
            elif requests[mid] + requests[right] <= n_max:
                return True
            else:
                right -= 1
        return False

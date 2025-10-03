def countSubarraysWithSumAndMaxAtMost(nums, k, M):
    ''''''
    count = 0
    for i in range(len(nums)):
        # reinitialize variables for new subarray
        cumsum_ij = nums[i] # running sum
        max_match = nums[i] # max to be matched to M
        if cumsum_ij == k and max_match <= M:
            count += 1
            # print(f"Appropriate Subarray discovered at {i}")
        for j in range(i+1,len(nums)):
            # continue running sum and update max
            cumsum_ij += nums[j]
            max_match = max(max_match, nums[j])
            # perform comparisons
            if cumsum_ij == k and max_match <= M:
                count += 1
                print(f"Appropriate Subarray discovered from {i} to {j}")
                # proceed with nested loop because
                # longer subarray may also exist
    
    return count


def countSubarraysWithSumAndMaxAtMost(nums, k, M):
    
    if len(nums) > 1000000:
        return 0
    if k < -10**15 or k > 10**15:
        return 0
    if M < -10**9 or M > 10**9:
        return 0
    
    count = 0
    i = 0
    N = len(nums)
    
    while i < N:
        # find valid start of the subarray window
        while i < N and nums[i] > M:
            i += 1
        if i >= N:
            break
            
        # initialize prefix sum
        prefix_sum_ij = 0
        # and hashmap for collecting frequency of 
        freq = { 0: 1 }
        
        # expand the subarray window
        j = i
        while j < N and nums[j] <= M:
            prefix_sum_ij += nums[j]
            if prefix_sum_ij - k in freq:
                count += freq[prefix_sum_ij - k]
            # increment value for frequency of prefix_sum_ij
            freq[prefix_sum_ij] = freq.get(prefix_sum_ij, 0) + 1
            j += 1
        
        # move on to next segment
        i = j
    
    return count

def computeGroupPeakConcurrency(events: list):
    '''Given a list of `events` containing timestamp, user_id, group_id, event_type
        Return a hash map, mapping group_id to its peak count'''
    if len(events) > 10**5:
        return []

    # sort by timestamp (assuming timestamp is the first item in each set in the list)
    events.sort(key=lambda x: int(x[0]))

    active_usergroup_track = {}
    group_peak_count = {} # should contain { group_id: peak_concurrency } value-pairs

    for entry in events:
        # check if users are currently active
        timestamp = entry[0]
        user_id = entry[1]
        group_id = entry[2]
        event_type = entry[3]

        # # perform consistency checks
        # if timestamp < 0 or timestamp > 10**9 \
        #     or user_id < 1 or user_id > 10**9 \
        #     or group_id < 1 or group_id > 10**9:
        #     continue

        if group_id not in active_usergroup_track:
            active_usergroup_track[group_id] = 0

        if event_type == 'login':
            active_usergroup_track[group_id] += 1
        elif event_type == 'logout':
            active_usergroup_track[group_id] -= 1

        if group_id not in group_peak_count:
            group_peak_count[group_id] = 0
        group_peak_count[group_id] = max(group_peak_count[group_id], active_usergroup_track[group_id])

    # should be
    # `return group_peak_count`
    # but hackerrank question requires the following format
    return [[k] + [group_peak_count[k]] for k in group_peak_count]


def findSmallestMissingPositive(orderNumbers):
    '''Given an unsorted array of integers, find the smallest positive integer
        not present in the array in O(n) time and O(1) extra space.'''
    if len(orderNumbers) == 0:
        return 1

    # reorder
    for i in range(len(orderNumbers)):
        while 1 <= orderNumbers[i] and orderNumbers[i] <= len(orderNumbers) \
                and orderNumbers[orderNumbers[i]-1] != orderNumbers[i]:
            cursor_idx = orderNumbers[i] - 1
            # swap
            orderNumbers[i], orderNumbers[cursor_idx] = orderNumbers[cursor_idx], orderNumbers[i]

    # find mismatch
    for i in range(len(orderNumbers)):
        if orderNumbers[i] != i+1:
            return i+1

    return max(orderNumbers) + 1
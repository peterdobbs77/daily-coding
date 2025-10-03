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
    active_usergroup_track = {}
    group_peak_count = {}

    for entry in events:
        # check if users are currently active
        timestamp = entry[0]
        user_id = entry[1]
        group_id = entry[2]
        event_type = entry[3]

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

# if __name__ == '__main__':

#     nums, k, M = [2, -1, 2, 1, -2, 3], 3, 2
#     print(f"{countSubarraysWithSumAndMaxAtMost(nums, k, M)} == 2")
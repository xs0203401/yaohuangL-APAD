
# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo").

    # dictionary key as websites
    # values are the list of users
    sites = {}
    for n in range(len(site_list)):
        if (site_list[n] not in sites):
            sites[site_list[n]]=[]
        sites[site_list[n]].append(user_list[n])

    # make pairs for items in the dict
    # and check users intersection
    sites_items = tuple(sites.items())
    max_affinity_num = 0
    max_affinity_pair = ['a','b']
    for i in range(len(sites)):
        for j in range(i+1, len(sites)):
            affinity_num = len(set(sites_items[i][1]) & set(sites_items[j][1]))
            # try to avoid using "intersection" operation:
            # affinity_num = sum([1 for x in set(sites_items[j][1]) if x in sites_items[i][1]])
            if (max_affinity_num < affinity_num):
                max_affinity_num = affinity_num
                max_affinity_pair = sorted([sites_items[i][0], sites_items[j][0]])

    return (max_affinity_pair[0], max_affinity_pair[1])

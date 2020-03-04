# Adapted from http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html#eight-queens-puzzle-part-1


def queens_share_diagonal(x0, y0, x1, y1):
    """ Does (x0,y0) share a diagonal with (x1,y1)? """
    ydist = abs(y1-y0)
    xdist = abs(x1-x0)
    return ydist == xdist

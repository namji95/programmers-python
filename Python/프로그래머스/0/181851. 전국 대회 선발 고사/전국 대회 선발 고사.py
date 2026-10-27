def solution(rank, attendance):
    rerank = []
    for r, a in zip(rank, attendance):
        if a:
            rerank.append(r)
    rerank.sort()
    return 10000 * rank.index(rerank[0]) + 100 * rank.index(rerank[1]) + rank.index(rerank[2])
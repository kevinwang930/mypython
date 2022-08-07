from functools import reduce
  
MAX_ATTACH_NUM = 2
money, goods_num = [int(x) for x in input().split()]
money //= 10
  
goods = []
attach_goods = set()
calc_results = {}
  
attach_record = []
  
for i in range(goods_num):
    price, weight, attach_index = [int(x) for x in input().split()]
    price //= 10
    weight *= price
    goods.append([price, weight, []])
    if attach_index:
        attach_record.append([attach_index - 1, i])
        # goods[attach_index - 1][-1].append(i)
        attach_goods.add(i)
  
for i,attach_index in attach_record:
    goods[i][-1].append(attach_index)
  
# print(goods)
  
  
def calc_result(g_num, m):
    if not g_num or m <= 0:
        return 0
  
    if (g_num -1) in attach_goods:
        return calc_result(g_num - 1, m)
  
    now = calc_results.get((g_num, m))
    if now is not None:
        return now
  
    p, w, atts = goods[g_num - 1]
    if m >= p:
        max_weight = max([calc_result(g_num - 1, m - p) + w, calc_result(g_num - 1, m)])
    else:
        max_weight = calc_result(g_num -1, m)
  
    things = [goods[i] for i in atts]
    att_cost = sum([x[0] for x in things])
    att_weight = sum([x[1] for x in things])
  
    if len(atts) > 0:
        max_weight = max(calc_result(g_num - 1, m - things[0][0] - p) + w + things[0][1], max_weight) if m >= p + things[0][0] else max_weight
  
    if len(atts) > 1:
        max_weight = max(calc_result(g_num - 1, m - things[1][0] - p) + w + things[1][1], max_weight) if m >= p + things[1][0] else max_weight
        max_weight = max(calc_result(g_num - 1, m - things[1][0] - things[0][0] - p) + w + things[1][1] + things[0][1], max_weight) if m >= p + things[1][0] + things[0][0] else max_weight
  
  
    # possibles = {}
    #
    # def get_possible(deep, total_set):
    #     if not deep: return [[]]
    #     now_ps = possibles.get(deep)
    #     if now_ps != None: return now_ps
    #
    #     less_ps = get_possible(deep - 1, total_set)
    #     current_possibles = [l_p + [x] for l_p in less_ps  for x in total_set - set(l_p) if x > (max(l_p) if l_p else 0)]
    #
    #     possibles[deep] = current_possibles
    #     return current_possibles
    #
    #
    # pss = reduce(lambda a,b: a+b, [get_possible(x, set(atts)) for x in range(MAX_ATTACH_NUM + 1)], [])
    # c_att_weight = 0
    # if g_num == 1:
    #     print(possibles.values())
    # for ps in pss:
    #     things = [goods[i] for i in ps]
    #     att_cost = sum([x[0] for x in things])
    #     att_weight = sum([x[1] for x in things])
    #
    #     if m >= att_cost + p:
    #         c_att_weight = max(c_att_weight, att_weight)
    #
    # max_weight += c_att_weight
  
    calc_results[(g_num, m)] = max_weight
  
    return max_weight
  
  
print(calc_result(goods_num, money) * 10)
# print(calc_results)
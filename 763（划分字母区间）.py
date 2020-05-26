class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        from operator import itemgetter
        if not S:
            return []
        if len(S) == 1:
            return [1]
        min_inf, max_inf = 0, 10000
        # 记录各节点的出现的最大位置和最小位置
        str_dict = dict()
        for index, s in enumerate(S):
            str_dict.setdefault(s, dict())
            str_dict[s]["max"] = max(str_dict[s].get("max", min_inf), index)
            str_dict[s]["min"] = min(str_dict[s].get("min", max_inf), index)
        # 排序
        data_list = list(str_dict.values())
        data_list.sort(key=itemgetter("min", "max"))

        result_list = list()
        for index, data in enumerate(data_list):
            # 起始位置
            if not index:
                minn, maxx = data.get("min"), data.get("max")
                continue
            # 结束位置
            if index + 1 == len(data_list):
                if minn < data.get("min") and maxx < data.get("min"):
                    result_list.append(maxx - minn + 1)
                    result_list.append(data.get("max") - data.get("min") + 1)
                else:
                    minn, maxx = min(data.get("min"), minn), max(data.get("max"), maxx)
                    result_list.append(maxx - minn + 1)
                continue
            # 边界判断
            if minn < data.get("min") and maxx < data.get("min"):
                result_list.append(maxx - minn + 1)
                minn, maxx = data.get("min"), data.get("max")
            else:
                # 更新最大值和最小值
                minn, maxx = min(data.get("min"), minn), max(data.get("max"), maxx)
        return result_list


if __name__ == '__main__':
    print(Solution().partitionLabels("befrppytljbvezqkjzkvmncnc"))
    print(Solution().partitionLabels("eaaaabaaec"))
    print(Solution().partitionLabels("ababcbacadefegdehijhklij"))

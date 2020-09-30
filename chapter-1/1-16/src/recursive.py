#!/usr/bin/env python3

from fractions import Fraction


def try_result(nums: list, target: Fraction = 24) -> str:
    # print("called with", nums, "target at", target)
    if len(nums) < 2:
        if Fraction(nums[0]) == target:
            return str(nums[0])
        else:
            return None

    for i in range(len(nums)):
        spec = Fraction(nums[i])
        nums.remove(spec)
        if rsp := try_result(nums, target + spec):
            return "(%s)-%d" % (rsp, spec)
        if rsp := try_result(nums, spec - target):
            return "%d-(%s)" % (spec, rsp)
        if rsp := try_result(nums, target - spec):
            return "(%s)+%d" % (rsp, spec)
        if spec != Fraction(0):
            if rsp := try_result(nums, target / spec):
                return "(%s)*%d" % (rsp, spec)
        if target != Fraction(0):
            if rsp := try_result(nums, spec / target):
                return "%d/(%s)" % (spec, rsp)
        if rsp := try_result(nums, target * spec):
            return "(%s)/%d" % (rsp, spec)

        nums.insert(i, spec)

    return None

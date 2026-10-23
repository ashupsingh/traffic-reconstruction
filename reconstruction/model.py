"""New reconstruction, 2026-10-23. Demo inputs are synthetic, not historical results."""
def allocate_green(queues, green_budget=60, minimum=10):
    if not queues or any(q<0 for q in queues) or green_budget<len(queues)*minimum:raise ValueError('Infeasible plan')
    remaining=green_budget-len(queues)*minimum;total=sum(queues)
    return [minimum+remaining*(q/total if total else 1/len(queues)) for q in queues]
def compare_delay(baseline, candidate):
    if baseline<=0 or candidate<0:raise ValueError('Invalid delay')
    return 100*(baseline-candidate)/baseline
def demo():
    plan=allocate_green([10,30]);assert abs(sum(plan)-60)<1e-8 and min(plan)>=10
    assert allocate_green([0,0])==[30,30]
    return {'synthetic_green_plan_seconds':plan,'road_controller':False,'measured_congestion_reduction':None}

if __name__ == "__main__":
    import json
    print(json.dumps(demo(), indent=2))

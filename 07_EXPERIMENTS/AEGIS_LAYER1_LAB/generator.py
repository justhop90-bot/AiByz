from itertools import product

FACT_CLASSES = ("direct_state", "derived", "feasibility", "relational")
MUTATIONS = ("none", "source_change", "source_change_then_refresh", "source_change_then_delay")
TIMES = (0, 1, 4, 8, 16, 32)
REPLICATES = range(1, 13)


def persistent_fact_matrix(build, limit=None):
    cases = product(FACT_CLASSES, MUTATIONS, TIMES, REPLICATES)
    for index, (fact_class, mutation, delay, replicate) in enumerate(cases, 1):
        if limit is not None and index > limit:
            break
        yield {
            "experiment_id": f"P0A-FRESH-{index:05d}",
            "question": "Does fact F retain its prior value after controlled source mutation?",
            "hypotheses": ["live", "scheduled", "cached", "explicit_refresh", "fact_class_specific"],
            "build_fingerprint": build,
            "independent_variable": {
                "fact_class": fact_class,
                "mutation": mutation,
                "delay": delay,
                "replicate": replicate,
            },
            "promotion_target": "P0-A",
        }

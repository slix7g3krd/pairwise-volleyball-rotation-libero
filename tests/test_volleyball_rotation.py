import pytest
import gameplay.volleyball_rotation as mod

CASES = [
    ("rotation_atomic_commit", (1,)),
    ("challenge_rollback_position", (1,)),
    ("libero_slot_isolate", (1,)),
    ("block_touch_count", (1,)),
    ("server_round_clock", (1,)),
    ("ball_swept_landing", (1,)),
    ("load_court", (1,)),
    ("register_lineup", (1,)),
    ("advance_rally", (1,)),
    ("present_rally", (1,)),
    ("validate_rally", (1,)),
    ("metrics_rally", (1,)),
    ("audit_rally", (1,)),
    ("fallback_rally", (1,)),
    ("determinism_rally", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None

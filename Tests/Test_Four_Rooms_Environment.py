from Four_Rooms_Environment import Four_Rooms_Environment
from random import randint


def test_location_to_state():
    """Tests location_to_state maps each location to a unique integer"""
    for num_rows in [6, 10]:
        for num_cols in [6, 9]:
            env = Four_Rooms_Environment(grid_width=num_cols, grid_height=num_rows)
            observed_states = set()
            for row in range(num_rows):
                for col in range(num_cols):
                    state = env.location_to_state((row, col))
                    assert state not in observed_states
                    observed_states.add(state)

def test_actions_execute_correctly():
    """Tests that actions execute correctly"""
    env = Four_Rooms_Environment(stochastic_actions_probability=0.0)
    env.move_user(env.current_user_location, (3, 3))

    env.conduct_action(0)
    assert env.current_user_location == (2, 3)

    env.conduct_action(1)
    assert env.current_user_location == (2, 4)

    env.conduct_action(2)
    assert env.current_user_location == (3, 4)

    env.conduct_action(3)
    assert env.current_user_location == (3, 3)

    env.conduct_action(0)
    assert env.current_user_location == (2, 3)

    env.conduct_action(0)
    assert env.current_user_location == (1, 3)

    env.conduct_action(0)
    assert env.current_user_location == (1, 3)

    env.conduct_action(1)
    assert env.current_user_location == (1, 4)

    env.conduct_action(1)
    assert env.current_user_location == (1, 5)

    env.conduct_action(1)
    assert env.current_user_location == (1, 5)

def test_check_user_location_and_goal_location_match_state_and_next_state():
    """Checks whether user location always matches state and next state correctly"""
    for _ in range(50):
        env = Four_Rooms_Environment()
        for _ in range(50):
            move = randint(0, 3)
            env.conduct_action(move)
            assert env.state == env.location_to_state(env.current_user_location)
            assert env.next_state == env.location_to_state(env.current_user_location)

def test_lands_on_goal_correctly():
    """Checks whether getting to goal state produces the correct response"""
    env = Four_Rooms_Environment(stochastic_actions_probability=0.0)
    env.move_user(env.current_user_location, (3, 3))
    env.current_goal_location = (2, 2)

    env.conduct_action(2)
    assert env.get_reward() == -1.0
    assert not env.get_done()

    env.conduct_action(3)
    assert env.get_reward() == 100.0
    assert not env.get_done()



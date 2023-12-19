import streamlit as st

# Define your equations as functions
def rotor_cross_sectional_area(d):
    return (3.14 * d ** 2) / 4

def stator_cross_sectional_area(d, e):
    return (3.14 * d ** 2) / 4 + 4 * e * d

def fluid_flow_area(e, d):
    return 4 * e * d

def theoretical_flow_rate(e, d, n, P_s):
    return 4 * e * d * n * P_s

def actual_flow_rate(q_t, q_s):
    return q_t - q_s

def volumetric_efficiency(q_a, q_t):
    return q_a / q_t

def rotational_speed_design(q_tl, Q_t):
    return q_tl / Q_t

def production_rate_design(n, Q_t):
    return n * Q_t

def rotational_speed_design_with_slip(n, Q_t, q_s):
    return n * Q_t - q_s

# Streamlit interface
st.title("PCP Design Calculator")

# Add input fields for parameters
d = st.number_input("Enter diameter (d)", value=0.0)
e = st.number_input("Enter eccentricity (e)", value=0.0)
n = st.number_input("Enter rotational speed (n)", value=0.0)
P_s = st.number_input("Enter pitch of the stator (P_s)", value=0.0)
q_t = st.number_input("Enter theoretical flow rate (q_t)", value=0.0)
q_s = st.number_input("Enter slip flow rate (q_s)", value=0.0)
q_tl = st.number_input("Enter total liquid production rate (q_tl)", value=0.0)
Q_t = st.number_input("Enter theoretical flow rate at 100 RPM (Q_t)", value=0.0)

# Calculation button
if st.button("Calculate"):
    A_rotor = rotor_cross_sectional_area(d)
    A_stator = stator_cross_sectional_area(d, e)
    A_f = fluid_flow_area(e, d)
    q_t = theoretical_flow_rate(e, d, n, P_s)
    q_a = actual_flow_rate(q_t, q_s)
    E_v = volumetric_efficiency(q_a, q_t)
    n_design = rotational_speed_design(q_tl, Q_t)
    q_tl_design = production_rate_design(n, Q_t)
    n_design_slip = rotational_speed_design_with_slip(n, Q_t, q_s)

    # Display results
    st.write(f"Rotor Cross-Sectional Area: {A_rotor}")
    st.write(f"Stator Cross-Sectional Area: {A_stator}")
    st.write(f"Fluid Flow Area: {A_f}")
    st.write(f"Theoretical Flow Rate: {q_t}")
    st.write(f"Actual Flow Rate: {q_a}")
    st.write(f"Volumetric Efficiency: {E_v}")
    st.write(f"Rotational Speed Design: {n_design}")
    st.write(f"Production Rate Design: {q_tl_design}")
    st.write(f"Rotational Speed Design considering slip: {n_design_slip}")

   
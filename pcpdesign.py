import streamlit as st
import numpy as np

# Define the main function of the Streamlit app
def main():
    st.title("Progressive Cavity Pump Design Calculator")

    # Inputs
    d = st.number_input("Enter the rotor minor diameter (d) in inches:", min_value=0.0, format="%.2f")
    e = st.number_input("Enter the eccentricity (e) in inches:", min_value=0.0, format="%.2f")
    Ps = st.number_input("Enter the stator pitch length (Ps) in inches:", min_value=0.0, format="%.2f")
    n = st.number_input("Enter the rotational speed (n) in RPM:", min_value=0.0, format="%.2f")
    qs = st.number_input("Enter the volumetric slip rate (qs) in B/D:", min_value=0.0, format="%.2f")

    # Additional condition for fluid type
    fluid_type = st.selectbox("Select the fluid type:", ["Corrosive", "Non-Corrosive"])

    # Calculations
    if st.button("Calculate"):
        # Calculating various parameters based on the provided equations
        A_rotor = np.pi * d**2 / 4
        A_stator = A_rotor + 4 * e * d
        A_f = 4 * e * d
        qt = A_f * n * Ps
        qa = qt - qs
        Ev = qa / qt

        # Displaying results
        st.write(f"Rotor Cross-Sectional Area (A_rotor): {A_rotor:.2f} in²")
        st.write(f"Stator Cross-Sectional Area (A_stator): {A_stator:.2f} in²")
        st.write(f"Fluid Flow Area (A_f): {A_f:.2f} in²")
        st.write(f"Theoretical Displacement Rate (qt): {qt:.2f} B/D")
        st.write(f"Actual Flow Rate (qa): {qa:.2f} B/D")
        st.write(f"Volumetric Efficiency (Ev): {Ev:.2f}")

        # Material recommendation based on fluid type
        if fluid_type == "Corrosive":
            st.write("Material Recommendation: Use corrosion-resistant materials like stainless steel or special alloys.")
        else:
            st.write("Material Recommendation: Standard materials like carbon steel are sufficient.")

# Run the app
if __name__ == "__main__":
    main()

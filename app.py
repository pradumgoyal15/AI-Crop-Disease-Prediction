            st.write(
                f"**{what_is_it}**"
            )

            st.write(
                info["description"]
            )

            st.write(
                f"**{common_symptoms}**"
            )

            st.write(
                info["symptoms"]
            )

            st.write(
                f"**{management}**"
            )

            st.write(
                info["management"]
            )

        else:

            st.write(
                no_info
            )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

        # =================================================
        # MODEL INFORMATION
        # =================================================

        st.divider()

        st.subheader(
            model_title
        )

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"**{model_text.split(':')[0]}:** "
                f"{model_text.split(':')[1].strip()}"
            )

        with col2:

            st.write(
                f"**{classes_text.split(':')[0]}:** "
                f"{classes_text.split(':')[1].strip()}"
            )

        st.write(
            dataset_text
        )

        # =================================================
        # DISCLAIMER
        # =================================================

        st.warning(
            disclaimer
        )


# =========================================================
# PREDICTION HISTORY
# =========================================================

st.divider()
st.subheader("🗂️ Prediction History")

history = st.session_state.prediction_history

if history:
    st.dataframe(history, use_container_width=True)

    # Download CSV report
    csv_buffer = io.StringIO()
    writer = csv.DictWriter(csv_buffer, fieldnames=history[0].keys())
    writer.writeheader()
    writer.writerows(history)

    st.download_button(
        label="⬇️ Download Prediction History (CSV)",
        data=csv_buffer.getvalue(),
        file_name="crop_disease_prediction_history.csv",
        mime="text/csv",
    )

    if st.button("🧹 Clear History"):
        st.session_state.prediction_history = []
        st.rerun()
else:
    st.caption("Your analyzed images and predictions will appear here during this session.")

# =========================================================
# FOOTER
# =========================================================

st.divider()

if language == "हिन्दी":

    st.caption(
        "AI फसल रोग पहचान प्रणाली | "
        "Python, TensorFlow और Streamlit से बनाया गया"
    )

else:

    st.caption(
        "AI Crop Disease Prediction System | "
        "Built with Python, TensorFlow & Streamlit"
    )

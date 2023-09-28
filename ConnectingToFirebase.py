# Import Necessary Libraries
!pip install pyrebase
import streamlit as st
import pandas as pd
import pyrebase
import matplotlib.pyplot as plt

# Firebase configuration
config = {
    "apiKey": "AIzaSyDhG1eFQVO5rwfvR75aRd740aXDRY2CO7E",
    "authDomain": "healthcare-system-a5329.firebaseapp.com",
    "databaseURL": "https://healthcare-system-a5329-default-rtdb.firebaseio.com",
    "projectId": "healthcare-system-a5329",
    "storageBucket": "healthcare-system-a5329.appspot.com",
    "messagingSenderId": "12287639804",
    "appId": "1:12287639804:web:d6fea27f432053d8275779",
    "measurementId": "G-HX45R78Y1J"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(config)
database = firebase.database()

# Set Streamlit App Title and Page Icon
st.set_page_config(
    page_title="Hospital Healthcare System",
    page_icon="🏥",
    layout="wide",  # To make the app wider
    initial_sidebar_state="expanded"  # To expand the sidebar by default
)

# Add a Title with Dark Blue Background
st.title("Hospital Healthcare System")
st.markdown(
    '<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>',
    unsafe_allow_html=True
)
st.markdown(
    '<style>div.row-widget.stRadio > div{flex-direction:row;}</style>',
    unsafe_allow_html=True
)
st.markdown(
    '<style>div.Widget.row-widget.stCheckbox > div{flex-direction:row;}</style>',
    unsafe_allow_html=True
)

# Set Light Grey Background Color
st.markdown(
    """
    <style>
    body {
        background-color: #f2f2f2; /* Light grey color code */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Get record types
record_types = ["Patient Record", "Medicine_Record", "Facility Record", "Fall Detect Record"]
selected_record_type = st.selectbox("Select a Record Type", record_types, help="Select the type of healthcare record.")

record = database.child("Record").child(selected_record_type).get().val()

if selected_record_type == "Patient Record":

    if record:
        # Get user input to choose a key
        selected_key = st.selectbox("Select a Patient", list(record.keys()), help="Select a patient's record.")

        # Extract data for the selected key
        selected_data = record[selected_key]

        # Initialize lists to store data
        date_list = []
        time_list = []
        id_list = []
        temperature_list = []
        water_level_list = []

        # Iterate through the nested dictionaries and extract data
        for date, date_data in selected_data.items():
            for time, time_data in date_data.items():
                for _id, id_data in time_data.items():
                    date_list.append(date)
                    time_list.append(time)
                    id_list.append(_id)
                    temperature_list.append(id_data.get('Temperature', 0))
                    water_level_list.append(id_data.get('Water_Level', 0))

        # Create a DataFrame
        df = pd.DataFrame({
            'Date': date_list,
            'Time': time_list,
            'ID': id_list,
            'Temperature': temperature_list,
            'Water_Level': water_level_list
        })

        # Combine Date and Time into a DateTime column
        df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
        df.set_index('DateTime', inplace=True)

        # Display the DataFrame table
        st.write("### Selected Data:")
        st.write(df)

        # Create subplots for two separate graphs
        fig1, ax1 = plt.subplots(figsize=(12, 5))
        fig2, ax2 = plt.subplots(figsize=(12, 5))

        # Plot Water Level
        ax1.plot(df.index, df['Water_Level'], label='Water Level', color='blue')
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Water Level')
        ax1.set_title('Water Level Time Series')
        ax1.grid(True)  # Add grid lines for better readability

        # Plot Temperature
        ax2.plot(df.index, df['Temperature'], label='Temperature', color='red')
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Temperature')
        ax2.set_title('Temperature Time Series')
        ax2.grid(True)  # Add grid lines for better readability

        # Display legends
        ax1.legend()
        ax2.legend()

        # Adjust layout and display the plots in Streamlit
        plt.tight_layout()

        # Add headers and descriptions
        st.write("### Water Level Graph:")
        st.pyplot(fig1)
        st.write("### Temperature Graph:")
        st.pyplot(fig2)

elif selected_record_type == "Medicine_Record":

    if record:
        # Get user input to choose a key
        selected_key = st.selectbox("Select a Patient", list(record.keys()), help="Select a patient's record.")

        # Extract data for the selected key
        selected_data = record[selected_key]

        # Initialize lists to store data
        date_list = []
        time_list = []
        id_list = []
        humidity_list = []
        MTemp_list = []

        # Iterate through the nested dictionaries and extract data
        for date, date_data in selected_data.items():
            for time, time_data in date_data.items():
                for _id, id_data in time_data.items():
                    date_list.append(date)
                    time_list.append(time)
                    id_list.append(_id)
                    humidity_list.append(id_data.get('humidity', 0))
                    MTemp_list.append(id_data.get('temperature', 0))

        # Create a DataFrame
        df = pd.DataFrame({
            'Date': date_list,
            'Time': time_list,
            'ID': id_list,
            'Humidity': humidity_list,
            'Temperature': MTemp_list
        })

        # Combine Date and Time into a DateTime column
        df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
        df.set_index('DateTime', inplace=True)

        # Display the DataFrame table
        st.write("### Selected Data:")
        st.write(df)

        # Create subplots for two separate graphs
        fig1, ax1 = plt.subplots(figsize=(12, 5))
        fig2, ax2 = plt.subplots(figsize=(12, 5))

        # Plot Water Level
        ax1.plot(df.index, df['Humidity'], label='Humidity', color='blue')
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Humidity')
        ax1.set_title('Humidity Time Series')
        ax1.grid(True)  # Add grid lines for better readability

        # Plot Temperature
        ax2.plot(df.index, df['Temperature'], label='Temperature', color='red')
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Temperature')
        ax2.set_title('Temperature Time Series')
        ax2.grid(True)  # Add grid lines for better readability

        # Display legends
        ax1.legend()
        ax2.legend()

        # Adjust layout and display the plots in Streamlit
        plt.tight_layout()

        # Add headers and descriptions
        st.write("### Humidity Graph:")
        st.pyplot(fig1)
        st.write("### Temperature Graph:")
        st.pyplot(fig2)

elif selected_record_type == "Facility Record":

    if record:
        # Get user input to choose a key
        selected_key = st.selectbox("Select a Patient", list(record.keys()), help="Select a patient's record.")

        # Extract data for the selected key
        selected_data = record[selected_key]

        # Initialize lists to store data
        date_list = []
        time_list = []
        id_list = []
        AQ_list = []
        Light_list = []
        Hum_list = []
        Temp_list = []

        # Iterate through the nested dictionaries and extract data
        for date, date_data in selected_data.items():
            for time, time_data in date_data.items():
                for _id, id_data in time_data.items():
                    date_list.append(date)
                    time_list.append(time)
                    id_list.append(_id)
                    AQ_list.append(id_data.get('Air Quality', 0))
                    Light_list.append(id_data.get('Light', 0))
                    Hum_list.append(id_data.get('humidity', 0))
                    Temp_list.append(id_data.get('temperature', 0))

        # Create a DataFrame
        df = pd.DataFrame({
            'Date': date_list,
            'Time': time_list,
            'ID': id_list,
            'Air Quality': AQ_list,
            'Light': Light_list,
            'Humidity': Hum_list,
            'Temperature': Temp_list
        })

        # Combine Date and Time into a DateTime column
        df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
        df.set_index('DateTime', inplace=True)

        # Display the DataFrame table
        st.write("### Selected Data:")
        st.write(df)

        # Create subplots for two separate graphs
        fig1, ax1 = plt.subplots(figsize=(12, 5))
        fig2, ax2 = plt.subplots(figsize=(12, 5))
        fig3, ax3 = plt.subplots(figsize=(12, 5))
        fig4, ax4 = plt.subplots(figsize=(12, 5))

        # Plot Water Level
        ax1.plot(df.index, df['Air Quality'], label='Air Quality', color='blue')
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Air Quality')
        ax1.set_title('Air Quality Time Series')
        ax1.grid(True)  # Add grid lines for better readability

        # Plot Temperature
        ax2.plot(df.index, df['Light'], label='Light', color='red')
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Light')
        ax2.set_title('Light Time Series')
        ax2.grid(True)  # Add grid lines for better readability

         # Plot Water Level
        ax3.plot(df.index, df['Humidity'], label='Humidity', color='blue')
        ax3.set_xlabel('Time')
        ax3.set_ylabel('Humidity')
        ax3.set_title('Humidity Time Series')
        ax3.grid(True)  # Add grid lines for better readability

        # Plot Temperature
        ax4.plot(df.index, df['Temperature'], label='Temperature', color='red')
        ax4.set_xlabel('Time')
        ax4.set_ylabel('Temperature')
        ax4.set_title('Temperature Time Series')
        ax4.grid(True)  # Add grid lines for better readability

        # Display legends
        ax1.legend()
        ax2.legend()
        ax3.legend()
        ax4.legend()

        # Adjust layout and display the plots in Streamlit
        plt.tight_layout()

        # Add headers and descriptions
        st.write("### Air Quality Graph:")
        st.pyplot(fig1)
        st.write("### Light Graph:")
        st.pyplot(fig2)
        # Add headers and descriptions
        st.write("### Humidity Graph:")
        st.pyplot(fig3)
        st.write("### Temperature Graph:")
        st.pyplot(fig4)

elif selected_record_type == "Fall Detect Record":

    if record:
        # Get user input to choose a key
        selected_key = st.selectbox("Select a Patient", list(record.keys()), help="Select a patient's record.")

        # Extract data for the selected key
        selected_data = record[selected_key]

        # Initialize lists to store data
        date_list = []
        time_list = []
        id_list = []
        distance_list = []
        motion_list = []

        # Iterate through the nested dictionaries and extract data
        for date, date_data in selected_data.items():
            for time, time_data in date_data.items():
                for _id, id_data in time_data.items():
                    date_list.append(date)
                    time_list.append(time)
                    id_list.append(_id)
                    distance_list.append(id_data.get('distance', 0))
                    motion_list.append(id_data.get('motion', 0))

        # Create a DataFrame
        df = pd.DataFrame({
            'Date': date_list,
            'Time': time_list,
            'ID': id_list,
            'Distance': distance_list,
            'Motion': motion_list,
        })

        # Combine Date and Time into a DateTime column
        df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
        df.set_index('DateTime', inplace=True)

        # Display the DataFrame table
        st.write("### Selected Data:")
        st.write(df)

        # Create subplots for two separate graphs
        fig1, ax1 = plt.subplots(figsize=(12, 5))

        # Plot Water Level
        ax1.plot(df.index, df['Distance'], label='Distance', color='blue')
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Distance')
        ax1.set_title('Distance Time Series')
        ax1.grid(True)  # Add grid lines for better readability

        # Display legends
        ax1.legend()

        # Adjust layout and display the plots in Streamlit
        plt.tight_layout()

        # Add headers and descriptions
        st.write("### Distance Graph:")
        st.pyplot(fig1)

else:
    st.warning("No records found for the selected type. Please select another record.")


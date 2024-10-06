import streamlit as st
import pickle
import base64


def add_bg_from_local(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_string});
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


def set_bg_from_url(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({image_url});
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def home_page():
    set_bg_from_url("https://cdn.wallpapersafari.com/18/89/ubnCGX.jpg")


    st.markdown(
        """
        <div style='display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; padding: 20px;'>
            <h1 style='font-size: 72px; margin: 0; white-space: nowrap;'>Forest Type Detection</h1>
            <p style='font-size: 24px; text-align: center; margin-top: 20px; max-width: 800px; padding: 0 20px;'>Welcome to the Forest Type Detection web app. Navigate through the tabs to explore the features.</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def prediction_page():

    set_bg_from_url("https://wallpaperaccess.com/full/4224720.jpg")

    st.title("Prediction Page")


    Elevation = st.text_input("Enter the elevation", 2596)
    Aspect = st.text_input("Enter the direction that slope faces", 50)
    slope = st.text_input("Enter the degree of incline of terrain", 3)
    hdth = st.text_input("Enter the horizontal distance to water body", 258)
    vdth = st.text_input("Enter the vertical distance to nearest water body", 0)
    hdtr = st.text_input("Enter the horizontal distance to nearest road ", 510)
    h9 = st.text_input("Enter the amount of sunlight reaching surface at 9 AM", 221)
    hn = st.text_input("Enter the amount of sunlight reaching surface at noon", 230)
    h3 = st.text_input("Enter the amount of sunlight reaching surface at 3 PM", 148)
    hdtfp = st.text_input("Enter the horizontal distance to nearest fire point", 6279)
    a1 = st.radio(' Whether the location is in a designated wilderness area, affecting land use and ecological protection.', options=['Yes', 'No'])
    a2 = st.radio('Whether the location is in a designated wilderness area,  have any conservation practices', options=['Yes', 'No'])
    a3 = st.radio('Whether the location is in a designated wilderness area, delineating conservation efforts.', options=['Yes', 'No'])
    a4 = st.radio('Whether the location is in a designated wilderness area, a protected ecological zones.', options=['Yes', 'No'])
    if a1=="Yes":
        wa1=1
    else:
        wa1=0

    if a2=="Yes":
        wa2=1
    else:
        wa2=0

    if a2=="Yes":
        wa3=1
    else:
        wa3=0

    if a4=="Yes":
        wa4=1
    else:
        wa4=0

    features = [Elevation, Aspect, slope, hdth, vdth, hdtr, h9, hn, h3, hdtfp, wa1, wa2, wa3, wa4]


    scalar = pickle.load(
        open('C://Users//Siva G Nair//PycharmProjects//pythonProject//Project//project2//assets//models//scale.sav',
             'rb'))
    model = pickle.load(
        open('C://Users//Siva G Nair//PycharmProjects//pythonProject//Project//project2//assets//models/model.sav',
             'rb'))

    predict = st.button("PREDICT")

    if predict:
        result = model.predict(scalar.transform([features]))
        st.session_state['result'] = result  # Store the result in session state
        st.session_state['page'] = 'Result'  # Redirect to result page
        st.experimental_rerun()  # Trigger a rerun


def result_page():

    set_bg_from_url("https://wallpaperaccess.com/full/1595911.jpg")

    st.title("Prediction Result")

    if 'result' in st.session_state:
        result = st.session_state['result']

        if result == 1:
            st.markdown(
                """
                ## Spruce/Fir Forest 
                Spruce/Fir forests are primarily composed of spruce (Picea spp.) and fir (Abies spp.) species. These forests typically thrive in colder, mountainous regions where precipitation is high. Their resilience to frost and snow allows them to survive in such extreme environments.
                """)
            st.image("https://swall.teahub.io/photos/small/281-2813569_spruce-fir-forest.jpg",
                     caption="Spruce/Fir Forest")
        elif result == 2:
            st.markdown(
                """
                ## 2.Lodgepole Pine Forest
                Lodgepole Pine forests are known for their resilience and rapid regrowth after wildfires. They are found across the western United States and Canada. Lodgepole pines grow densely and are often subject to fire cycles that rejuvenate the forest ecosystem.
                """)
            st.image("https://i.pinimg.com/736x/14/eb/76/14eb761bf249238bfbce19b23a0cbcb2.jpg",
                     caption="Lodgepole Pine Forest")
        elif result == 3:
            st.markdown(
                """
                ## Ponderosa Pine Forest 
                Ponderosa Pine forests are iconic for their thick, fire-resistant bark and open canopies. They are common in the western United States and are a crucial part of fire-adapted ecosystems. The trees are often found in drier regions with frequent wildfires.
                """)
            st.image(
                "https://thumbs.dreamstime.com/b/forest-ponderosa-pine-trees-oregon-old-growth-central-96709374.jpg",
                caption="Ponderosa Pine Forest")
        elif result == 4:
            st.markdown(
                """
                ## Cottonwood/Willow Forest 
                Cottonwood/Willow forests thrive in riparian zones along rivers and floodplains. They provide critical habitat for wildlife and are essential for maintaining biodiversity. Cottonwoods grow rapidly in moist environments, while willows contribute to soil stabilization.
                """)
            st.image(
                "https://fthmb.tqn.com/vh44xN6H5ilFNYtCs9esxbhphOU=/960x0/filters:no_upscale()/171371653-56a98cbf5f9b58b7d0fca204.jpg",
                caption="Cottonwood/Willow Forest")
        elif result == 5:
            st.markdown(
                """
                ## 5.Aspen Forest 
                Aspen forests are known for their bright white bark and vibrant fall colors. Aspens are clonal trees, meaning they reproduce primarily through root sprouts, creating vast networks of genetically identical trees. These forests are often found at higher elevations.
                """)
            st.image("https://wallpapercave.com/wp/wp5762392.jpg", caption="Aspen Forest")
        elif result == 6:
            st.markdown(
                """
                ## Douglas-fir Forest 
                Douglas-fir forests are among the most valuable for timber production. They are found in the Pacific Northwest and are prized for their fast growth and strong, durable wood. These forests play an essential role in the timber economy and ecological health.
                """)
            st.image(
                "https://islandnature.ca/wp-content/uploads/2013/05/arbutus-douglas-fir-ruckle-provincial-park.jpg",
                caption="Douglas-fir Forest")
        elif result == 7:
            st.markdown(
                """
                ## Mixed Conifer Forest 
                Mixed Conifer forests feature a diverse mix of conifer species, including pines, firs, and cedars. These forests are highly biodiverse and can be found across the western United States. They offer essential habitat for a wide range of wildlife.
                """)
            st.image(
                "https://www.researchgate.net/profile/Tandin-Tandin/publication/361659203/figure/fig7/AS:1172909225721865@1656654759833/A-mixed-conifer-forest-stand-in-western-Bhutan.png",
                caption="Mixed Conifer Forest")
    else:
        st.write("The result will appear here.")


def page_navigation():

    st.sidebar.title("Navigation")
    option = st.sidebar.radio("Go to", ["Home", "Prediction", "Result", "Documentation", "About"])


    if option == "Home":
        home_page()
    elif option == "Prediction":
        prediction_page()
    elif option == "Result":
        result_page()
    elif option == "Documentation":
        documentation_page()
    elif option == "About":
        about_page()


# Documentation Page
def documentation_page():

    st.markdown(
        """
        <style>
            .doc-title {
                font-size: 36px; 
                font-weight: bold; 
                text-align: center; 
                margin-bottom: 20px; 
                font-family: 'Arial', sans-serif; 
            }
            .doc-text {
                font-size: 18px; 
                line-height: 1.6;
                margin: 10px 0; 
                padding: 0 20px; 
                text-align: left; 
                font-family: 'Georgia', serif; 
            }
            .doc-link {
                color: #1E90FF; 
                text-decoration: underline; 
                transition: color 0.3s;
            }
            .doc-link:hover {
                color: #FF4500; 
            }
        </style>
        """,
        unsafe_allow_html=True
    )


    st.markdown("<h1 class='doc-title'>Documentation</h1>", unsafe_allow_html=True)


    st.markdown("<p class='doc-text'>Here you can find the documentation and relevant links:</p>",
                unsafe_allow_html=True)


    st.markdown(
        "<p class='doc-text'><a class='doc-link' href='https://archive.ics.uci.edu/dataset/31/covertype'>Dataset</a> - This is the dataset used for forest type detection.</p>",
        unsafe_allow_html=True)


    st.markdown(
        "<p class='doc-text'><a class='doc-link' href='https://colab.research.google.com/drive/1hnl2waR1oI1mfGlNCIeEptwKZZ536inj?usp=sharing'>Ipynb</a> - This link directs to the Google Colab Notebook for the project.</p>",
        unsafe_allow_html=True)


    st.markdown(
        "<p class='doc-text'><a class='doc-link' href='https://github.com/SivaG2002/Forest-Species-Prediction'>UI</a> - This is the GitHub repository for the UI of the Forest Species Prediction app.</p>",
        unsafe_allow_html=True)



def about_page():
    st.title("About")


    st.markdown(
        """
        <style>
            h2 {
                font-size: 28px;  
                margin-bottom: 10px;  
            }
            p {
                font-size: 18px;  
                line-height: 1.6;  
                font-family: 'Arial', sans-serif;  
            }
            .title {
                margin-bottom: 20px;  
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="title">
        <h2>Project Overview:</h2>
        </div>
        <p>The Forest Type Detection app aims to classify forest types based on various environmental factors such as elevation, aspect, slope, and more. This tool assists ecologists and environmental scientists in understanding and predicting forest ecosystems.</p>

        <div class="title">
        <h2>Technologies Used:</h2>
        </div>
        <p>This project is built using Python and the Streamlit framework. It utilizes machine learning libraries such as Scikit-learn for predictive modeling and Pandas for data manipulation.The algorithm used are Random Forest and Decision Tree.From these Random Forest was chosen which gave an accuracy of 95%.</p>

        <div class="title">
        <h2>Features:</h2>
        </div>
        <p>Key features include:</p>
        <ul>
            <li>User-friendly input forms for entering environmental data.</li>
            <li>Instant predictions with detailed descriptions of each forest type.</li>
            <li>Visual representations of the results.</li>
        </ul>

        <div class="title">
        <h2>Dataset:</h2>
        </div>

        <p>The model is trained on the Covertype Dataset, which is from the <a href="https://archive.ics.uci.edu/" target="_blank">UC Irvine Machine Learning Repository</a>. It contains data on various forest cover types and related environmental attributes.</p>
        """,
        unsafe_allow_html=True
    )


def main():

    page_navigation()



main()




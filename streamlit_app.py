import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
import streamlit_authenticator as stauth
from streamlit.components.v1 import iframe
import time

def period_counter(list1,list4,n):
    index = list1.index(n)
    per=list4[index]
    return per


newhtml="""
            <!DOCTYPE html>
            <header></header>
            <style>
               .css-1v3fvcr{background: rgb(34,193,195);
                background: radial-gradient(circle, rgba(34,193,195,1) 46%, rgba(229,229,184,1) 100%);
                }
                div.css-nlntq9.e16nr0p33 p{background-color:white;
                }
                .css-nlntq9.e16nr0p33{}
                .block-container.css-12oz5g7.egzxvld2{background-color:white;
                    border:5px solid orange;
                    border-radius:15px;
                    margin-top:67px;
                }
                .css-6awftf.e19lei0e1{ display:none;}

                .title{}
                .css-1cpxqw2.edgvbvh5{background-color:orange;
                    color: white;
                }
                .css-1cpxqw2.edgvbvh5:focus{background-color:white;
                    color: orange;
                    font-weight:bold;
                    border:3px solid orange;

                }
            
            </style>
            <body> 
            </body
        """
st.markdown(newhtml,unsafe_allow_html=True)


# names = ['MARIA	TERZI','Στεριανή Αβράμη','ΔΕΣΠΟΙΝΑ ΑΒΡΑΜΙΔΟΥ','Μαρία Αγάθου']
# usernames = ['Maria-terzi@hotmail.com','stella-a88@hotmail.com','depi1970@hotmail.com','magathou@hotmail.com']
# passwords = ['tSYcA8GPCJ','hj2cJpZLXG','u46UXerHf9','pJH9CA7L2g']

html_logo = "<img style='display:block; margin-left:auto; margin-right:auto; text-align:center;' src='http://inclusiveeducation.eu/wp-content/uploads/2021/03/logoiam400x400.png'  width=300 height=300>"



st.markdown(html_logo, unsafe_allow_html=True)



names=['ΤΕΡΕΖΑ ΙΩΑΝΝΑ ΨΥΛΛΑΚΗ', 'Άννα Σαμίου', 'Αντιγόνη Μούντζελου', 'ΘΕΟΔΩΡΑ ΜΑΡΙΝΑΤΟΥ', 'ΑΛΕΞΑΝΔΡΑ ΠΑΠΑΔΗΜΗΤΡΙΟΥ', 'Χρυσούλα Σκλαβενίτη', 'ΒΑΪΑ ΠΑΠΑΓΕΩΡΓΙΟΥ', 'Κατερίνα Κοντακτσή', 'Χριστίνα Τάτση', 'ΠΑΣΧΑΛΙΤΣΑ ΔΟΚΟΠΟΥΛΟΥ', 'Καλιτσουνάκη Κατερίνα', 'Άννα Μπαξεβάνη', 'ΕΙΡΗΝΗ-ΣΤΕΡΓΙΑΝΗ ΚΟΥΝΤΟΥΡΑ', 'Ευδοκία Φιδανάκη', 'ΣΟΦΙΑ ΔΙΤΣΟΥΔΗ', 'ΑΝΝΑ ΚΙΡΚΟΥΔΗ', 'Κλεονίκη Κατωγιάννη', 'Σημέλα Παπαδοπούλου', 'Ειρήνη Γραφάκου', 'ΒΑΓΙΑ ΜΑΝΤΕΛΑ', 'ΒΑΣΙΛΙΚΗ ΜΙΧΑΛΟΠΟΥΛΟΥ', 'Κυριακή Φωτιάδου', 'Αναστασία Μαυρίδου', 'Μαρία Καλεμκερίδου', 'ΝΙΚΟΛΙΑ ΤΣΙΑΚΟΥ', 'Γεώργιος Μπαντής', 'ΑΝΑΣΤΑΣΙΑ ΜΠΟΥΛΟΥΚΗ', 'ΜΑΡΙΝΑ ΛΑΜΠΑΚΗ', 'Ζωή Χύτα', 'ΧΡΙΣΤΙΝΑ ΠΑΛΑΙΟΛΟΓΟΥ', 'ΘΕΟΔΟΡΑ ΣΙΣΜΑΝΙΔΟΥ', 'ΤΡΙΑΝΤΑΦΥΛΛΙΑ ΔΙΑΜΑΝΤΗ', 'ΓΕΩΡΓΙΑ ΤΣΑΜΗ', 'Πηγή Μπάρμπα', 'ΦΩΤΙΟΣ ΠΑΝΑΓΙΩΤΟΠΟΥΛΟΣ', 'Ευαγγελία Παπαδοπούλου', 'ΑΛΕΞΑΝΔΡΑ ΚΑΡΑΚΩΣΤΑ', 'Βαλεντίνη Αντωνία Τσιροπούλου', 'ΠΕΤΡΟΒΑ ΠΑΡΑΣΚΕΥΗ', 'ΔΗΜΗΤΡΑ ΘΕΟΔΩΡΑΚΟΠΟΥΛΟΥ', 'Ειρήνη Δολαψάκη', 'ΚΩΝΣΤΑΝΤΙΝΙΑ ΝΤΟΝΤΗ', 'Μαρία Καρχαριδου', 'Ζωή Μουλαρά', 'Γαρυφαλιά Χαϊδοπούλου', 'ΔΗΜΗΤΡΑ ΚΑΛΟΓΡΑΙΑΚΗ', 'ΕΙΡΗΝΗ ΠΑΝΑΓΙΩΤΟΥ', 'ΜΑΡΙΑ ΧΑΛΑΡΗ', 'ΠΑΡΑΣΚΕΥΑΣ ΚΟΥΚΟΣ', 'Βασιλική Παπά', 'ΑΙΚΑΤΕΡΙΝΗ ΚΑΤΣΟΥΓΙΑΝΝΗ', 'ΔΗΜΗΤΡΑ ΔΟΥΖΔΑΜΠΑΝΗ', 'ΑΝΝΑ ΤΖΩΡΤΖΑΤΟΥ', 'Θεοδωρα Λιάγκα', 'Ελένη Μπούζτου', 'ΚΑΛΛΙΟΠΗ ΜΠΟΧΤΗ', 'Δέσποινα Σούρλα', 'ΔΙΜΗΤΡΑ ΜΑΚΑΡΟΝΗ', 'Δήμητρα Παλέγκα', 'ΔΕΣΠΟΙΝΑ ΠΑΡΑΣΤΑΤΙΔΟΥ', 'ΙΩΑΝΝΑ ΖΩΗ ΡΟΥΣΣΟΥ', 'Ειρήνη Ζούμπου', 'ΑΝΑΣΤΑΣΙΑ ΚΙΚΙΛΙΓΚΑ', 'ΕΛΠΙΣ ΣΟΥΙΚΛΙΩΤΗ', 'ΣΤΥΛΙΑΝΗ ΚΟΥΜΠΕΝΑΚΗ', 'Κυριακή Πασχαλίδου', 'ΠΑΡΑΣΚΕΥΗ ΚΑΡΑΝΙΚΟΛΑ', 'Μαρία Πλιόγκα', 'Θεοδώρα Σισμανίδου', 'ΚΡΥΣΤΑΛΛΙΑ ΚΟΥΙΔΟΥ', 'ΔΗΜΗΤΡΗΣ ΣΑΒΒΑΚΗΣ', 'ΠΑΝΑΓΙΩΤΑ ΠΑΠΑΔΟΠΟΥΛΟΥ', 'Σοφία Τσιράκη', 'Κωνσταντια Δραγκα', 'ΜΑΡΙΑ ΚΙΑΓΙΑ', 'Ελένη Ευτυχία Κωστίδη']
usernames=['tpsyllaki@gmail.com', 'samanna82@gmail.com', 'antigonimountzelou@gmail.com', 'dmarinatou@gmail.com', 'alexpap070399@gmail.com', 'crissperly@gmail.com', 'papageorgiou_vaia@yahoo.gr', 'katkonta@gmail.com', 'achristinatatsi@gmail.com', 'linadokopou@yahoo.gr', 'kkalitsounaki@gmail.com', 'annabaxe87@gmail.com', 'eirinikoun@gmail.com', 'fidanaki123@gmail.com', 'sofi53@windowslive.com', 'anna.kirkoudi@gmail.com', 'niki.katogianni@gmail.com', 'simelapap@gmail.com', 'egrafakou@gmail.com', 'csioannina@yahoo.gr', 'vamix2007@yahoo.gr', 'kikifotiad@gmail.com', 'anastmavr@gmail.com', 'mia123kal4@gmail.com', 'nikitsiakou@gmail.com', 'bantisg1@otenet.gr', 'anboulouki@gmail.com', 'marinae_mail@yahoo.gr', 'zoichyta@gmail.com', 'buzantio@hotmail.com', 'theodora_sismanidou@hotmail.com', 'rose.diamanti@gmail.com', 'gt88_@hotmail.com', 'pigibarmpa@hotmail.com', 'panagiotoglou2@gmail.com', 'epapadop13@gmail.com', 'alexandrakarakosta.ak@gmail.com', 'tsiropoulou.valentini@gmail.com', 'vivaki_1993@yahoo.gr', 'theodorakopoulou.psy@gmail.com', 'eirhnhdol@gmail.com', 'kntonti2014@gmail.com', 'karxaridoumaria27@gmail.com', 'zoemoulara@gmail.com', 'litsa.xaidopoulou@gmail.com', 'didaorestiada@gmail.com', 'eirpan2203@yahoo.com', 'mariachalari83@gmail.com', 'parikouko@gmail.com', 'vasiapapa@gmail.com', 'katsougiannik@gmail.com', 'dimitradouzdampani@gmail.com', 'tzortzatou@gmail.com', 'theodoraliaga2003@gmal.com', 'bouztoue@gmail.com', 'kelly.bochti@yahoo.com', 'dsourla@yahoo.gr', 'dimitramakslt@gmail.com', 'dimitra.pal1@hotmail.com', 'tetaparastatidou@yahoo.gr', 'gz.roussou@hotmail.com', 'eirinizoumpou@yahoo.gr', 'anastasia.x.kikiligka@gmail.com', 'elpsou@gmail.com', 'stkoubenaki@yahoo.gr', 'dpashalidou@yahoo.gr', 'panagiotiskitis@yahoo.gr', 'mariaplioga@gmail.com', 'theodora.sismanidou9@gmail.com', 'krystalk.dask@yahoo.gr', 'savvakisd@gmail.com', 'papadopa3@gmail.com', 'sofiats87@gmail.com', 'dragakonstantia@gmail.com', 'marouli1980@yahoo.gr', 'ekostide@gmail.com']
passwords=['z8vGFDBMAQ', 'L6cZWVmsu8', 'SJ6pHmh7Ck', 'C8fexZT4R6', 'Hkw4mA3ZLF', 's8FEaD4cnB', 'u8amQwTbSX', 'mfwYVs6F2C', 'cz24J8fEKh', 'q3PSAeUnba', 'fA32gRKkXs', 'zcT5ZD6GsU', 'ZYf6e8tSXp', 'adWLg2ZUAV', 'vqwZS97Td2', 'AfTM7s9NpF', 'CpN8BKV2g4', 'nBzEkMy2jR', 'T3HK8f2wJg', 't7wezY2kPd', 'AKbn43mHY8', 'a7Z8duAUpD', 'bu9SEjGyfY', 'jv6Ek4rTgy', 'mMDd5Ra48f', 'UKqQjgaT9x', 'GESLcDg7jv', 'UDMgpm8zJR', 'x6tsTVapr5', 'u3ajr4kARH', 'QZe4xc2ATW', 'FdC95n2ZVw', 'G3VfyYQk9a', 'TEQ4xHvCt9', 'Mt9YH4jqeb', 'AP3xcv2VhX', 'XqpwB9Yv36', 'D85kt7GqfB', 'gpvK2b93Hq', 'zmwjbV3PTs', 'JTwkqVm2Kv', 'fq3cQWnjLR', 'zp35YamjRk', 'bwTXtGj4AZ', 'FC5vzgNrEL', 'KJE3PHhysB', 'A9xQmcH8jJ', 'j2K3hyV76L', 'bu5dhCHMcm', 'wmzHq8pWJG', 'EfTp8J5Duc', 'bTD58pkXCM', 'FZ5JYXnrMW', 'Q6537xmUrC', 'L2SkFNRn63', 'b6Yds7VLqk', 'bDUqJS4gLs', 'PJeuq3KH5p', 'hayN4S5KXV', 'c9uPY7fKbt', 'L6TbYtG274', 'WEVHfGnt2v', 'CXbg9QFMaw', 'Wz2YvXraCx', 'dVLJx5qRjS', 'sT3Q8PEVBx', 'dN5xw4h7Vq', 'dhpmqKQX9G', 'Ye69CpUFxq', 'Sd69btzrYy', 'g2PjzQxk9y', 'BMQ8fz2dc3', 'f4JHZBprSG', 'UrYqaAP3RM', 'yaXBdn6ATM', 'HqyK874k2g']
periods=['2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου']




# hashed_passwords = stauth.hasher(passwords).generate()
hashed_passwords = stauth.hasher(passwords).generate()

authenticator = stauth.authenticate(names,usernames,hashed_passwords,'some_cookie_name','some_signature_key',cookie_expiry_days=30)


name, authentication_status = authenticator.login('Login','main')



if authentication_status:
        # newhtml="""
        #     <!DOCTYPE html>
        #     <header></header>
        #     <style>
        #        .css-1v3fvcr{background: rgb(34,193,195);
        #         background: radial-gradient(circle, rgba(34,193,195,1) 46%, rgba(229,229,184,1) 100%);
        #         }
        #         div.css-nlntq9.e16nr0p33 p{background-color:white;
        #         }
        #         .css-nlntq9.e16nr0p33{}
        #         .block-container.css-12oz5g7.egzxvld2{background-color:white;
        #             border:5px solid black;
        #             border-radius:15px;
        #             margin-top:67px;
        #         }

        #         .title{}
        #         .css-1cpxqw2.edgvbvh5{background-color:orange;
        #             color: white;
        #         }
            
        #     </style>
        #     <body> 
        #     </body
        # """

        html2="""
            <!DOCTYPE html>
            <header></header>
            <style>
               
            
            </style>
            <body> 
                <ul>
                    <li>Πατήστε στο κουμπί "δημιουργία πιστοποιητικού" για να δημιουργήσετε το πιστοποιητικό σας</li>
                    <li>Αφού δημιουργήσετε το πιστοποιητικό σας, πατήστε στο κουμπί "παραλαβή πιστοποιητικού" για να κατεβάσετε το πιστοποιητικό σας</li>
                </ul>
            </body
        """
        html3="""
            <!DOCTYPE html>
            <header></header>
 
            <body> 
               <h3 style="text-align:center;">🎓 Εκτυπώστε το πιστοποιητικό σας</h3>
            </body
        """
        # st.markdown(newhtml,unsafe_allow_html=True)
        st.write('Καλησπέρα, *%s*' % (name))
        perds=period_counter(names,periods,name)

        # st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")
        st.markdown(html3,unsafe_allow_html=True)

        st.markdown(html2,unsafe_allow_html=True)

        left, right = st.columns(2)

        # right.write("Here's the template we'll be using:")

        right.image("http://inclusiveeducation.eu/wp-content/uploads/2022/04/template.png", width=300)

        env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
        template = env.get_template("template.html")

        
        # left.write("Fill in the data:")
        form = left.form("template_form")
        student = name
        course="Report Generation in Streamlit"
        grade = 100
        period=perds
        submit = form.form_submit_button("Δημιουργία πιστοποιητικού")
        
        if submit:
            html = template.render(
                student=student,
                course=course,
                period=period,
                grade=f"{grade}/100",
                date=date.today().strftime("%B %d, %Y"),
            )

            pdf = pdfkit.from_string(html, False)
            st.balloons()

            right.success("🎉 Το πιστοποιητικό σας δημιουργήθηκε!")
            # st.write(html, unsafe_allow_html=True)
            # st.write("")
            right.download_button(
                "⬇️ Παραλαβή πιστοποιητικού",
                data=pdf,
                file_name="diploma.pdf",
                mime="application/octet-stream",
            )

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')


# if st.session_state['authentication_status']:
#     st.write('Welcome *%s*' % (st.session_state['name']))
#     st.title('Some content')
elif st.session_state['authentication_status'] == False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] == None:
    st.warning('Please enter your username and password')
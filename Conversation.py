conv = (
    (
        r"i have a question ?",
        ("Please ask, I can answers your question regarding the site or the course / contents we provide.",)
    ),
    
    (
        r"what is the intake of (.*) department|(.*) intake of (.*)",
        ("We have 60 vacancy for our %1 department",)
    ),
    (
        r"how is the college infrastructure|how (.*) infrastructure",
        ("our infrastructure consist of canteen, hostel, gymkhana, premises, tranport facility, central computing facility, and office",)
    ),
    (
        r"what is the address of college|what is the exact location of college|(.*) location of college",
        ("Karjat Konkan Gyanpeeth Shaiskshnik Sankul, Dahivali, Raigad, MS 410201",)
    ),
    (
        r"exactly how far is college from station ?|(.*)college from station",
        ("Approximatly 5-10 minutes by bus or riksha",)
    ),
    (
        r"what are the means of transport ?|(.*) transport (.*)",
        ("By riksha or by bus",)
    ),
    (
        r"how is the hostel facility ?|(.*) hostel facility",
        ("We can accomodate upto 50 students",)
    ),
    (
        r"can you please provide me the contact details|(.*) contact details|(.*) phone no",
        ("Yes sure, Phone No. : (02148) 222580, 223768",)
    ),

    (
        r"what is the timing of college ?|(.*)college timing",
        ("From Morning 8 am to 5 pm, and it varies according to your batch in which you are enrolled.",)
    ),
    (
        r"when does the college library opens ?|(.*)college library",
        ("It opens at 9 am in morning",)
    ),
    (
        r"what is the working time of office ?|(.*) time of office",
        ("Between 10 am - 5 pm",)
    ),

    (
        r"what is the fees structure ?| (.*) fees structure",
        ("Fee structure will be available to you in our office.",)
    ),
    (
        r"what is the institute code of kgce ?|(.*) institute code",
        ("EN 3198 is the institute code of our college.",)
    ),
    (
        r"is kgce NAAC accredited ?| (.*) naac (.*)",
        ("Yes, college has been awarded with B+ grade.",)
    ),
    (
        r"what are the placement opportunity in kgce ?| (.*) placement (.*)",
        ("https://kgce.edu.in/placement-summary/ This is the kgce placement record.",)
    ),
    (
        r"(.*) companies which comes for campus interview ?|(.*) companies (.*)",
        ("Yes, company like Sankey solutions, neosoft, syntel, RK edu are our top recruters.",)
    ),
    (
        r"can you provide me the academic calander of 2019-2020| (.*) academic calander",
        ("Yes, https://kgce.edu.in/wp-content/uploads/2019/07/Academic-Calendar-2019-20-odd.pdf",)
    ),
    (
        r"do you have any website|(.*) website",
        ("Yes, Here it is https://kgce.edu.in/",)
    ),
    (
        r"from where should i download additionl forms?| (.*) additionl infomation (.*)",
        ("https://kgce.edu.in/download/",)
    ),

    (
        r"who is the ceo of kgce ?| (.*) ceo (.*)",
        ("Mr.Pradeepchandra V.Shringarpure",)
    ),
    (
        r"what is the name of principal of the college ?| (.*) name of principal",
        ("Dr. Madhukar J. Lengare",)
    ),
    (
        r"what is the name of hod of it department ?| (.*) hod of it department| (.*) hod of it dep",
        ("Prof. Jitendra Patil",)
    ),

    (
        r"(.*) kgce| (.*) k.g.c.e",
        ("Konkan gyanpeeth college of engineering",)
    ),
    (
        r"how many department (.*)| (.*) many department (.*)",
        ("4, Information technology, Computer, Electronic & Telecommunications, and Mechanical.",)
    ),
    (
        r"how many labs are there in it department ?| (.*) labs in it department",
        ("5, computer network lab (01), database lab (02), analysis and design lab (03), signal and image processing lab (04), open source lab (05).",)
    ),
    (
        r"who is lab incharge of computer network lab ?| (.*) lab incharge of lab 1",
        ("Prof. V.M.Kharche",)
    ),
    (
        r"who is lab incharge of database lab ?| (.*) lab incharge of lab 2",
        ("Prof. A.W.Kale",)
    ),
    (
        r"who is lab incharge of analysis and design lab ?| (.*) lab incharge of lab 3",
        ("Prof. A.S.Kunte",)
    ),
    (
        r"who is lab incharge of signal and image processing lab ?| (.*) lab incharge of lab 4",
        ("Prof. Y.B.Salve",)
    ),
    (
        r"who is lab incharge of open source lab ?| (.*) lab incharge of lab 5",
        ("Prof. A.D.Palsodkar",)
    ),

    (
        r"where can i find result (.*)| (.*) find result (.*)",
        ("https://kgce.edu.in/it-result-statistics/",)
    ),
    (
        r"where can i find syllabus (.*) | (.*) find syllabus (.*)",
        ("https://kgce.edu.in/it-syllabus/",)
    ),
    (
        r"where can i find previous year question papers ?| (.*) question paper",
        ("https://kgce.edu.in/it-question-paper/",)
    ),
    (
        r"who is lab incharge of computer network lab?| (.*) lab incharge of lab 1",
        ("Hello %1, How are you today ?",)
    ),

    (
        r"hi|hey|hello",
        ("Hello, How can I help you!",)
    ),
    (
        r"my name is (.*)",
        ("Hello %1, How are you today ?",)
    ),
    (
        r"what is your name ?",
        ("My name is Chatbot",)
    ),
    (
        r"who are you ?",
        ("i am Chatbot. I try to answer questions, Sometimes i get them right. Sometimes i need additional help. I am designed to get better overtime. How can i help you ?",)
    ),
    (
        r"how are you ?",
        ("I'm doing good, How about You ?",)
    ),
    (
        r"sorry (.*)|sorry",
        ("Its alright","Its OK, never mind",)
    ),
    (
        r"i'm (.*) doing good",
        ("Nice to hear that","Alright :)",)
    ),
    (
        r"(.*) create you ?",
        ("Jay Kate created me using Python's NLTK library",)
    ),
    (
        r"how is weather in (.*)?",
        ("Weather in %1 is awesome like always",)
    ),
    (
        r"i work in (.*)?",
        ("%1 is an Amazing company, I have heard about it.",)
    ),
    (
        r"bye|quit",
        ("BBye take care. See you soon","It was nice talking to you. See you soon")
    ),
)
A brief description of models and reasons for designing them as they have been has been included below.

A School is made up of its school name and address, the names is unique for each school. A School can have many classrooms and this information is placed under the ClassRoom model, a given school should only have a unique name for each class room, at the moment no level or grade information has been included as this is not absolutely relevant. Grade information can be captured within the classroom name for now. A ClassRoom can have one teacher.

A School has three types of active users, they are teachers, students and principals. A generic model of SchoolProfile is created to represent the three users.The types of users will be captured in the ‘group’  field in the existing django user model. SchoolProfile also has a foreign key to School  and this is the only additional information to the user model.

The principal groups would be allowed access to a view which shows  a listing of all school profiles that share the same id as them and belong to the teacher groups.

A Quiz model is defined to store metadata related to the quiz. A quiz can be attempted multiple times, the value is set at allowed_attempts, timing information is added in case this a timed quiz.

A Quiz  is related to a classrooms via ActiveQuiz. The ActiveQuiz model is used to store currently active quizzes that were running and have run. Each class can have multiple quizzes initiated by that class's teacher and a quiz can be given to multiple classes so a ManytoMany relationship is used here.Students can choose to do a quiz based on what is offered to the student's class.

A Quiz is related to Students via StudentWork The StudentWork model stores information about the quizzes attempted by a student, if the quiz is incomplete, information is stored in the IncompleteQuiz  which stores choices made by the student that can be displayed to the student when the student attempts the quiz again. A student can take multiple active quizzes depending on the number of quizzes offered to her class and also depending on the number of classes she belongs to.

A Quiz is made up of Questions. A question has a description and an image field if needed. An additional tags (model not defined) field has been added to store search related metadata so that a quiz can be created with questions used in other quizzes.

The Choice model stores options for q given a particular question.A question can have multiple choices, the django view would take care to ensure that during question definition ateast one of the choices offered is the right one and this is indicated in the is_right field. If more than one choice is_right, the view would show checkboxes instead of radio buttons. An additional explanation tag is added so that the view can display right/wrong explanations related to a choice after the quiz has been submitted.

The QuizDefinition  stores the actual definition of the quiz. Questions can be part of many quizzes and a quiz can have multiple questions so a many to many relationship is defined on Questions. An additional section_name has been added if questions are to be categorized in some way.

The IncompleteQuiz model stores state information. A many to many relationship is used since state can have many choices made, and a particular choice could be in multiple states.It may be efficient to store state as a json blob in student history to avoid additional lookups in another model.


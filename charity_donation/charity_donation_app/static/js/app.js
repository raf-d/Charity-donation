document.addEventListener("DOMContentLoaded", function() {
  /**
   * HomePage - Help section
   */
  class Help {
    constructor($el) {
      this.$el = $el;
      this.$buttonsContainer = $el.querySelector(".help--buttons");
      this.$slidesContainers = $el.querySelectorAll(".help--slides");
      this.currentSlide = this.$buttonsContainer.querySelector(".active").parentElement.dataset.id;
      this.init();
    }

    init() {
      this.events();
    }

    events() {
      /**
       * Slide buttons
       */
      this.$buttonsContainer.addEventListener("click", e => {
        if (e.target.classList.contains("btn")) {
          this.changeSlide(e);
        }
      });

      /**
       * Pagination buttons
       */
      this.$el.addEventListener("click", e => {
        if (e.target.classList.contains("btn") && e.target.parentElement.parentElement.classList.contains("help--slides-pagination")) {
          this.changePage(e);
        }
      });
    }

    changeSlide(e) {
      e.preventDefault();
      const $btn = e.target;

      // Buttons Active class change
      [...this.$buttonsContainer.children].forEach(btn => btn.firstElementChild.classList.remove("active"));
      $btn.classList.add("active");

      // Current slide
      this.currentSlide = $btn.parentElement.dataset.id;

      // Slides active class change
      this.$slidesContainers.forEach(el => {
        el.classList.remove("active");

        if (el.dataset.id === this.currentSlide) {
          el.classList.add("active");
        }
      });
    }

    /**
     * TODO: callback to page change event
     */
    changePage(e) {
      e.preventDefault();
      const page = e.target.dataset.page;

      console.log(page);
    }
  }
  const helpSection = document.querySelector(".help");
  if (helpSection !== null) {
    new Help(helpSection);
  }

  /**
   * Form Select
   */
  class FormSelect {
    constructor($el) {
      this.$el = $el;
      this.options = [...$el.children];
      this.init();
    }

    init() {
      this.createElements();
      this.addEvents();
      this.$el.parentElement.removeChild(this.$el);
    }

    createElements() {
      // Input for value
      this.valueInput = document.createElement("input");
      this.valueInput.type = "text";
      this.valueInput.name = this.$el.name;

      // Dropdown container
      this.dropdown = document.createElement("div");
      this.dropdown.classList.add("dropdown");

      // List container
      this.ul = document.createElement("ul");

      // All list options
      this.options.forEach((el, i) => {
        const li = document.createElement("li");
        li.dataset.value = el.value;
        li.innerText = el.innerText;

        if (i === 0) {
          // First clickable option
          this.current = document.createElement("div");
          this.current.innerText = el.innerText;
          this.dropdown.appendChild(this.current);
          this.valueInput.value = el.value;
          li.classList.add("selected");
        }

        this.ul.appendChild(li);
      });

      this.dropdown.appendChild(this.ul);
      this.dropdown.appendChild(this.valueInput);
      this.$el.parentElement.appendChild(this.dropdown);
    }

    addEvents() {
      this.dropdown.addEventListener("click", e => {
        const target = e.target;
        this.dropdown.classList.toggle("selecting");

        // Save new value only when clicked on li
        if (target.tagName === "LI") {
          this.valueInput.value = target.dataset.value;
          this.current.innerText = target.innerText;
        }
      });
    }
  }
  document.querySelectorAll(".form-group--dropdown select").forEach(el => {
    new FormSelect(el);
  });

  /**
   * Hide elements when clicked on document
   */
  document.addEventListener("click", function(e) {
    const target = e.target;
    const tagName = target.tagName;

    if (target.classList.contains("dropdown")) return false;

    if (tagName === "LI" && target.parentElement.parentElement.classList.contains("dropdown")) {
      return false;
    }

    if (tagName === "DIV" && target.parentElement.classList.contains("dropdown")) {
      return false;
    }

    document.querySelectorAll(".form-group--dropdown .dropdown").forEach(el => {
      el.classList.remove("selecting");
    });
  });

  /**
   * Switching between form steps
   */
  class FormSteps {
    constructor(form) {
      this.$form = form;
      this.$next = form.querySelectorAll(".next-step");
      this.$prev = form.querySelectorAll(".prev-step");
      this.$step = form.querySelector(".form--steps-counter span");
      this.currentStep = 1;

      this.$stepInstructions = form.querySelectorAll(".form--steps-instructions p");
      const $stepForms = form.querySelectorAll("form > div");
      this.slides = [...this.$stepInstructions, ...$stepForms];

      this.init();
    }

    /**
     * Init all methods
     */
    init() {
      this.events();
      this.updateForm();
    }

    /**
     * All events that are happening in form
     */
    events() {
      // Next step
      this.$next.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep++;
          if(this.currentStep === 3){
            let cats = document.querySelectorAll('.category');
            console.log(cats);
            let zaznaczone_cats = [];
            cats.forEach(cat => {
              if(cat.checked){
                zaznaczone_cats.push(cat.value)
              }
            })
            console.log(zaznaczone_cats)
          }
          this.updateForm();

        });
      });

      // My code
      // Create table with checked categories
      let checked_categories_list = []
      let button1 = document.querySelector('.step1')
      button1.disabled = true
      let chosen_categories = document.querySelector('.chosen-categories')

      function categories_table() {
                  let categoria = {
              id:this.value,
              name:this.dataset.name
          };
        if (this.checked) {


          checked_categories_list.push(categoria);
          console.log(checked_categories_list)
          if (checked_categories_list.length !== 0) {
            button1.disabled = false
          }
        } else {
          let index = checked_categories_list.indexOf(categoria);
          if(index > -1) {
            checked_categories_list.splice(index, 1)
          }
          if (checked_categories_list.length === 0){
            button1.disabled = true
          }
          console.log(checked_categories_list)
        }
        // do poprawy
        chosen_categories.innerText = ''
        checked_categories_list.forEach(category => chosen_categories.innerText += category.name + ', ')
      }
      // Catch all categories and add event to each
      let all_categories_list = document.querySelectorAll('.category-element')

      all_categories_list.forEach(thing => {
        thing.addEventListener('change', categories_table)
      })


      // Catch quantity of bags
      let bags_quantity = document.querySelector('.bags-value')
      let button2 = document.querySelector('.step2')
      button2.disabled = true

      function return_bags_quantity() {
        console.log('Changed bags quantity:')
        console.log(bags_quantity.value)
        let bags = document.querySelector('.bags')
        bags.innerHTML = bags_quantity.value
        button2.disabled = bags_quantity.value <= 0;
      }

      bags_quantity.addEventListener('change', return_bags_quantity)

      // Chose the organisation
      // let all_organisations_list = document.querySelectorAll('.org')
      // let matching_organisations = []
      // function set_matching_organisations = all_organisations_list.forEach(org => {
      //   if(checked_categories_list.every(category = org.dataset.id.indexOf(category) >= 0) {
      //     matching_organisations.push(org)
      //   })
      // })

      let button3 = document.querySelector('.step3')
      button3.disabled = true

      function choose_organisation() {
        let chosen_organisation = ''
        if (this.checked) {
          chosen_organisation = this.value
          button3.disabled = false
          console.log('Chosen organisation:')
          console.log(chosen_organisation)
          let chosen_org = document.querySelector('.chosen-organisation')
          chosen_org.innerText = chosen_organisation
        }
      }

      let all_organisations = document.querySelectorAll('.organisation')

      all_organisations.forEach(org => {
        org.addEventListener('change', choose_organisation)
      })

      // Step 4
      let button4 = document.querySelector('.step4')
      button4.disabled = true
      let street = document.querySelector('.street')
      let confirmed_street = document.querySelector('.confirmed-street')

      street.addEventListener('input', chose_street)

      function chose_street() {
        confirmed_street.innerText = street.value
        check_valid()
      }

      let city = document.querySelector('.city')
      let confirmed_city = document.querySelector('.confirmed-city')

      city.addEventListener('input', chose_city)

      function chose_city() {
        confirmed_city.innerText = city.value
        check_valid()
      }

      let zipcode = document.querySelector('.zipcode')
      let confirmed_zipcode = document.querySelector('.confirmed-zipcode')

      zipcode.addEventListener('input', chose_zipcode)

      function chose_zipcode() {
        confirmed_zipcode.innerText = zipcode.value
        check_valid()
      }

      let phone = document.querySelector('.phone')
      let confirmed_phone = document.querySelector('.confirmed-phone')

      phone.addEventListener('input', chose_phone)

      function chose_phone() {
        confirmed_phone.innerText = phone.value
        check_valid()
      }

      let date = document.querySelector('.date')
      let confirmed_date = document.querySelector('.confirmed-date')

      date.addEventListener('input', chose_date)

      function chose_date() {
        confirmed_date.innerText = date.value
        check_valid()
      }

      let time = document.querySelector('.time')
      let confirmed_time = document.querySelector('.confirmed-time')

      time.addEventListener('input', chose_time)

      function chose_time() {
        confirmed_time.innerText = time.value
        check_valid()
      }

      let more_info = document.querySelector('.more_info')
      let confirmed_info = document.querySelector('.confirmed-info')

      more_info.addEventListener('input', chose_info)

      function chose_info() {
        confirmed_info.innerText = more_info.value
        check_valid()
      }

      function check_valid() {
        if (street.value !=='' & city.value !=='' & zipcode.value !=='' & phone.value !=='' &
            date.value !=='' & time.value !=='' & more_info.value !=='') {
          button4.disabled = false
        }
      }


      // Existing code
      // Previous step
      this.$prev.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep--;
          this.updateForm();
        });
      });

      // Form submit
      // this.$form.querySelector("form").addEventListener("submit", e => this.submit(e));
    }

    /**
     * Update form front-end
     * Show next or previous section etc.
     */
    updateForm() {
      this.$step.innerText = this.currentStep;

      // TODO: Validation

      this.slides.forEach(slide => {
        slide.classList.remove("active");

        if (slide.dataset.step == this.currentStep) {
          slide.classList.add("active");
        }
      });

      this.$stepInstructions[0].parentElement.parentElement.hidden = this.currentStep >= 6;
      this.$step.parentElement.hidden = this.currentStep >= 6;

      // TODO: get data from inputs and show them in summary
    }

    /**
     * Submit form
     *
     * TODO: validation, send data to server
     */
    submit(e) {
      e.preventDefault();
      this.currentStep++;
      this.updateForm();
    }
  }
  const form = document.querySelector(".form--steps");
  if (form !== null) {
    new FormSteps(form);
  }
});

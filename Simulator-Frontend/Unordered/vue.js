new Vue({
    el: "#hello-world-app",
    data() {
      return {
        msg: "Hello World!"
      }
    }
  });

  const app = new Vue({
    el: '#app',
    data: {
        file: '',
        getResult: undefined,
        postResult: undefined,
        samplePostData: {
          title: 'foo',
          body: 'bar',
          userId: 1
        }
    },
    methods: {
        handleFileUpload(){
          this.file = this.$refs.file.files[0];
        },
        submitFile(){
          /*
                  Initialize the form data
              */
              let formData = new FormData();
  
              /*
                  Add the form data we need to submit
              */
              formData.append('file', this.file);
  
          /*
            Make the request to the POST /single-file URL
          */
              axios.post( 'http://localhost:5000/post',
                  formData,
                  {
                  headers: {
                      'Content-Type': 'multipart/form-data'
                  }
                }
              ).then(function(response){
                console.log("lol"+this.getResult)
                console.log(response.data)
                this.getResult = response.data
                console.log(this.getResult)
                //this.getResult = response.data.json();
                console.log('SUCCESS!!');
                alert('File sent');
            
          })
          .catch(function(){
            console.log('FAILURE!!');
          });
        },
        getSampleData() {
            fetch('http://localhost:5000/')
                .then(response => response.json())
                .then((result) => {
                    // sample callback
                    this.getResult = result;
                    console.log(this.getResult)
                })
        },
        postSampleData() {
            fetch('https://jsonplaceholder.typicode.com/posts', {
              method: 'post',
              body: JSON.stringify(this.samplePostData)
            }).then((response) => response.json())
            .then((result) => {
            /* will return
              {
                id: 101
              }
              */
              this.postResult = result
            })
        }
    }
})
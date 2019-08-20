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
        getResult: undefined,
        postResult: undefined,
        samplePostData: {
          title: 'foo',
          body: 'bar',
          userId: 1
        }
    },
    methods: {
        getSampleData() {
            fetch('http://localhost:5000/')
                .then(response => response.json())
                .then((result) => {
                    // sample callback
                    this.getResult = result;
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
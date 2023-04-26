// crowdcount.js
function getCrowdCount() {
  $.post('/api/crowd_count', function(data) {
      // Update HTML with crowd count result
      console.log(data.result);  // Replace with your actual code to update the HTML
  });
}
// Example of sending data to the API endpoint from cad.html
var data = {
  value: 42  // Set the value to be sent to the backend
};

fetch('/api/data', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)  // Send data in JSON format
})
.then(response => response.json())
.then(data => {
  console.log(data.result);  // Process the response from the backend
})
.catch(error => {
  console.error('Error:', error);
});

// Function to perform counting logic and send data to backend
function countPeople() {
  // Perform counting logic here
  // This could involve analyzing the image, processing data, etc.

  // Example count result
  var count = 100;

  // Send count to backend
  fetch('/count', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ count: count }),
  })
    .then(response => response.json())
    .then(data => {
      // Update the result text element with the response from backend
      document.getElementById('resultText').innerText = 'Number of people in the crowd: ' + data.count;
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

// Add event listener to count button
document.getElementById('countButton').addEventListener('click', function() {
  countPeople();
  // frontend.js - Example code for making API calls from frontend

// Get form and result container elements
const form = document.getElementById('crowdForm');
const resultContainer = document.getElementById('resultContainer');

// Add event listener to form submit event
form.addEventListener('submit', async (event) => {
  event.preventDefault(); // Prevent form submission
  const countInput = document.getElementById('countInput').value;
  
  // Make POST request to backend API with count input data
  try {
    await axios.post('/api/crowdcount', { count: countInput });
    resultContainer.textContent = 'Crowd data added successfully';
  } catch (error) {
    console.error(error);
  }
});

// Make GET request to backend API on page load
window.addEventListener('load', async () => {
  try {
    const response = await axios.get('/api/crowdcount');
    const crowdData = response.data;
    // Handle response data and update UI accordingly
    console.log(crowdData);
  } catch (error) {
    console.error(error);
  }
});
})
/* 
document.getElementById("crowdCountbtn").onclick=function(){
  fun()
};
function fun(){
  const a= Math.random();
  console.log(a);
}



 */
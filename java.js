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

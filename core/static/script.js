// Get the form element
const ideaForm = document.getElementById('ideaForm');

// Submit event listener for the idea submission form
ideaForm.addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent form submission

  // Get form field values
  const name = document.getElementById('name').value;
  const department = document.getElementById('department').value;
  const email = document.getElementById('email').value;
  const title = document.getElementById('ideaTitle').value;
  const description = document.getElementById('description').value;
  const benefits = document.getElementById('benefits').value;
  const plan = document.getElementById('implementationPlan').value;
  const attachments = document.getElementById('attachments').files;

  // Create an object to store the idea details
  const idea = {
    name,
    department,
    email,
    title,
    description,
    benefits,
    plan,
    attachments
  };

  // Clear form fields
  ideaForm.reset();

  // Call a function to process the idea submission (e.g., send to the server)
  processIdeaSubmission(idea);
});

// Function to process the idea submission
async function processIdeaSubmission(idea) {
  // Perform actions to handle the idea submission (e.g., AJAX request to the server)
  console.log("Data",idea)
  const response = await fetch("/save", {
      method: "POST", 
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(idea),
    });
  // Display a success message
  displaySubmissionMessage('success', 'Idea submitted successfully!');
}

// Function to display a submission message
function displaySubmissionMessage(type, message) {
  const discussionDiv = document.getElementById('discussion');
  const messageDiv = document.createElement('div');
  messageDiv.className = type;
  messageDiv.textContent = message;
  discussionDiv.appendChild(messageDiv);
}

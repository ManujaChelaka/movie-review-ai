let myChart = null; // Variable to store the chart instance

async function analyzeReviews() {
    const btn = document.getElementById('analyzeBtn');
    const loading = document.getElementById('loading');
    const dashboard = document.getElementById('dashboard');

    // Show loading state and hide old dashboard
    btn.disabled = true;
    loading.classList.remove('hidden');
    dashboard.classList.add('hidden');

    try {
        const title = document.getElementById('movieInput').value || 'Inception';
        // Use the full URL to reach your Flask server on Port 5000
        const response = await fetch(`http://127.0.0.1:5000/analyze?title=${encodeURIComponent(title)}`);

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();

        // Update the stat cards using the names from your app.py return statement
        document.getElementById('totalReviews').innerText = data.total_reviews;
        document.getElementById('avgConfidence').innerText = data.overall_sentiment;
        document.getElementById('overallVerdict').innerText = data.ai_summary;

        // Show/Hide poster
        const posterImg = document.getElementById('moviePoster');
        if (data.poster_url) {
            posterImg.src = data.poster_url;
            posterImg.classList.remove('hidden');
        } else {
            posterImg.classList.add('hidden');
        }

        // Draw the visualization chart
        updateChart(data.positive, data.negative, data.neutral);

        // Show the results
        dashboard.classList.remove('hidden');

        // Populate detailed results
        const container = document.getElementById('reviewsContainer');
        container.innerHTML = '';
        data.detailed_results.forEach(res => {
            const div = document.createElement('div');
            div.className = `review-item ${res.sentiment.toLowerCase()}`;
            div.innerHTML = `
                <p>"${res.text}"</p>
                <span class="sentiment-tag">${res.sentiment} (${res.confidence}%)</span>
            `;
            container.appendChild(div);
        });
    } catch (error) {
        console.error("Connection failed:", error);
        alert("Backend server not running! Ensure app.py is active in the terminal.");
    } finally {
        loading.classList.add('hidden');
        btn.disabled = false;
    }
}

function updateChart(pos, neg, neu) {
    const ctx = document.getElementById('sentimentChart').getContext('2d');

    // Destroy previous chart to prevent glitches when clicking analyze again
    if (myChart) {
        myChart.destroy();
    }

    myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Positive', 'Negative', 'Neutral'],
            datasets: [{
                data: [pos, neg, neu],
                backgroundColor: ['#00d2ff', '#ff4b2b', '#94a3b8'],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { labels: { color: 'white' } }
            }
        }
    });
}
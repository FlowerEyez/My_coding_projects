// Pong Game Implementation
const canvas = document.getElementById("pong");
const ctx = canvas.getContext("2d");

// Game Constants
const PADDLE_WIDTH = 10, PADDLE_HEIGHT = 80;
const BALL_SIZE = 14;
const PLAYER_X = 20, AI_X = canvas.width - 20 - PADDLE_WIDTH;
const PADDLE_SPEED = 7;
const BALL_SPEED = 6;

// Game state
let playerY = canvas.height / 2 - PADDLE_HEIGHT / 2;
let aiY = canvas.height / 2 - PADDLE_HEIGHT / 2;
let ballX = canvas.width / 2 - BALL_SIZE / 2;
let ballY = canvas.width / 2 - BALL_SIZE / 2;
let ballVX = BALL_SPEED * (Math.random() < 0.5 ? 1 : -1);
let ballVY = BALL_SPEED * (Math.random() * 2 - 1);

function resetBall() {
    ballX = canvas.width / 2 - BALL_SIZE / 2;
    ballY = canvas.width / 2 - BALL_SIZE / 2;
    ballVX = BALL_SPEED * (Math.random() < 0.5 ? 1 : -1);
    ballVY = BALL_SPEED * (Math.random() * 2 - 1);
}

function drawRect(x, y, w, h, color) {
    ctx.fillStyle = color;
    ctx.fillRect(x, y, w, h);
}

function drawBall(x, y, size, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(x + size / 2, y + size / 2, size / 2, 0, Math.PI * 2);
    ctx.fill();
}

function drawNet() {
    ctx.setLineDash([10, 10]);
    ctx.strokeStyle = "#666";
    ctx.beginPath();
    ctx.moveTo(canvas.width / 2, 0);
    ctx.lineTo(canvas.width / 2, canvas.height);
    ctx.stroke();
    ctx.setLineDash([]);
}

function render() {
    //Background
    drawRect(0, 0, canvas.width, canvas.height, "#222");

    drawNet();

    // Paddles
    drawRect(PLAYER_X, playerY, PADDLE_WIDTH, PADDLE_HEIGHT, "#4caf50");
    drawRect(AI_X, aiY, PADDLE_WIDTH, PADDLE_HEIGHT, "#e91e63");

    // Ball
    drawBall(ballX, ballY, BALL_SIZE, "#fff");
}

function clamp(val, min, max) {
    return Math.max(min, Math.min(max, val));
}

// Mouse control for player paddle
canvas.addEventListener("mousemove", function(e) {
    const rect = canvas.getBoundingClientRect();
    const mouseY = e.clientY - rect.top;
    playerY = clamp(mouseY - PADDLE_HEIGHT / 2, 0, canvas.height - PADDLE_HEIGHT);
});

//simple AI for right paddle
function updateAI() {
    //Move AI paddle towards ball's Y position
    let target = ballY + BALL_SIZE / 2 - PADDLE_HEIGHT / 2;
    if (aiY < target) {
        aiY += PADDLE_SPEED;
    } else if (aiY > target) {
        aiY -= PADDLE_SPEED;
    }
    aiY = clamp(aiY, 0, canvas.height - PADDLE_HEIGHT);
}

function updateBall() {
    ballX += ballVX;
    ballY += ballVY;

    // Top/bottom wall collision
    if (ballY <= 0) {
        ballY = 0;
        ballVY = -ballVY;
    }
    if (ballY + BALL_SIZE >= canvas.height) {
        ballY = canvas.height - BALL_SIZE;
        ballVY = -ballVY;
    }

    //Left paddle collision
    if (
        ballX <= PLAYER_X + PADDLE_WIDTH &&
        ballY + BALL_SIZE >= playerY &&
        ballY <= playerY + PADDLE_HEIGHT
    ) {
        ballX = PLAYER_X + PADDLE_WIDTH;
        ballVX = -ballVX;
        // Add some spin based on paddle movement
        ballVY += ((ballY + BALL_SIZE / 2) - (playerY + PADDLE_HEIGHT / 2)) * 0.2;
    }

    // Right paddle collision
    if (
        ballX + BALL_SIZE >= AI_X &&
        ballY + BALL_SIZE >= aiY &&
        ballY <= aiY + PADDLE_HEIGHT
    ) {
        ballX = AI_X - BALL_SIZE;
        ballVX = -ballVX;
        ballVY += ((ballY + BALL_SIZE / 2) - (aiY + PADDLE_HEIGHT / 2)) * 0.2;
    }

    //Left/right wall (Score)
    if (ballX < 0 || ballX + BALL_SIZE > canvas.width) {
        resetBall();
    }
}

function gameLoop() {
    updateAI();
    updateBall();
    render();
    requestAnimationFrame(gameLoop);
}

resetBall();
gameLoop();
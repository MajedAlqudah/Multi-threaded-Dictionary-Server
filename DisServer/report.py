from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image


def create_report(file_path, dictionary):
    # Create a PDF document
    doc = SimpleDocTemplate(file_path, pagesize=letter)

    # Define custom styles
    styles = getSampleStyleSheet()
    heading1 = ParagraphStyle("Heading1", parent=styles["Heading1"], textColor=colors.blue, fontSize=16, spaceBefore=20)
    heading2 = ParagraphStyle("Heading2", parent=styles["Heading2"], textColor=colors.darkgreen, fontSize=14,
                              spaceBefore=10)
    body = ParagraphStyle("Body", parent=styles["BodyText"], textColor=colors.black, fontSize=12, spaceBefore=5)
    code = ParagraphStyle("Code", parent=styles["Code"], textColor=colors.brown, fontSize=10, spaceBefore=5)
    red_link = ParagraphStyle("RedLink", textColor=colors.red, fontSize=12, spaceBefore=5)

    # Add content to the PDF document
    content = []

    # Heading
    content.append(Paragraph("Multi-threaded Dictionary Server Report", heading1))
    content.append(Spacer(1, 20))

    # Server Architecture
    content.append(Paragraph("Server Architecture:", heading2))
    content.append(Paragraph("Our server follows a client-server architecture using sockets and threads. "
                             "It implements a multi-threaded design to handle concurrent client requests. "
                             "The server listens for incoming connections on a specified port and responds to "
                             "client queries with the meanings of words from the dictionary.", body))
    content.append(Spacer(1, 10))

    # Design Choices
    content.append(Paragraph("Design Choices:", heading2))
    content.append(Paragraph("- We chose to use Python for the implementation due to its simplicity and "
                             "extensive standard library support for networking and threading. "
                             "- We opted for a multi-threaded design to handle concurrent client requests. "
                             "- Error handling is implemented to manage network communication and data "
                             "processing errors.", body))
    content.append(Spacer(1, 10))

    # Features
    content.append(Paragraph("Features:", heading2))
    content.append(Paragraph("- Allows clients to query the meaning of a word. "
                             "- Supports concurrent connections using a worker pool architecture. "
                             "- Implements error handling for network communication and data processing. "
                             "- Provides a command-line interface for launching the server.", body))
    content.append(Spacer(1, 10))

    # Words Dictionary
    content.append(Paragraph("Words Dictionary:", heading2))
    for word, meanings in dictionary.items():
        content.append(Paragraph(f"<b>{word}:</b> {'; '.join(meanings)}", body))
    content.append(Spacer(1, 10))

    # Video Link
    content.append(Paragraph("Video Demo:", heading2))
    content.append(Paragraph(
        '<font color="red"><a href="https://drive.google.com/file/d/1U1xITWej5B8gukLH2XFwhx0spB9ecuPv/view?usp=sharing">Click here to watch the video demo</a></font>',
        red_link))
    content.append(Spacer(1, 10))

    # Code Snapshots
    content.append(Paragraph("Code Snapshots:", heading2))
    content.append(Paragraph("Server Implementation:", body))
    content.append(Image("server_code_snapshot.png", width=400, height=200))
    content.append(Spacer(1, 10))
    content.append(Paragraph("Client Implementation:", body))
    content.append(Image("client_code_snapshot.png", width=400, height=200))
    content.append(Spacer(1, 20))

    # Conclusion
    content.append(Paragraph("Conclusion:", heading2))
    content.append(Paragraph("Overall, our multi-threaded dictionary server provides a reliable and efficient "
                             "solution for querying word meanings concurrently. With its flexible architecture "
                             "and robust error handling, it meets the requirements of the project and demonstrates "
                             "the effective use of sockets and threads.", body))

    # Build PDF document
    doc.build(content)


if __name__ == "__main__":
    dictionary = {
        "hello": ["used as a greeting"],
        "world": ["the earth and all people and things on it"],
        "python": ["a large constricting snake found in tropical and subtropical regions"],
        "algorithm": ["a step-by-step procedure or set of rules for solving a problem or accomplishing a task"],
        "database": [
            "an organized collection of structured information or data, typically stored electronically in a computer system"],
        "framework": ["a basic structure underlying a system, concept, or text"],
        "encryption": [
            "the process of converting information or data into a code, especially to prevent unauthorized access"],
        "artificial intelligence": [
            "the theory and development of computer systems capable of performing tasks that typically require human intelligence"],
        "machine learning": [
            "a subset of artificial intelligence that focuses on the development of algorithms and statistical models that enable computers to learn and improve from experience"],
        "big data": [
            "extremely large datasets that may be analyzed computationally to reveal patterns, trends, and associations, especially relating to human behavior and interactions"],
        "cloud computing": [
            "the delivery of computing services, including servers, storage, databases, networking, software, and analytics, over the internet (the cloud) to offer faster innovation, flexible resources, and economies of scale"],
        "cybersecurity": [
            "the practice of protecting computer systems, networks, and data from digital attacks, unauthorized access, and other cyber threats"]
    }
    create_report("server_report.pdf", dictionary)

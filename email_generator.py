#!/usr/bin/env python3
"""
Email Generator - Creates professional, friendly emails from bullet points
"""

def main():
    print("=" * 50)
    print("📧 Email Generator")
    print("=" * 50)
    print()

    # Get recipient's name
    recipient_name = input("Who's the recipient? (e.g., Sarah, Dr. Smith): ").strip()

    # Get email subject
    subject = input("What's the subject line? ").strip()

    # Choose tone
    print("\nChoose your email tone:")
    print("  1. Formal")
    print("  2. Casual")
    print("  3. Friendly (default)")
    tone_choice = input("Enter 1, 2, or 3 (press Enter for friendly): ").strip()

    tone_map = {'1': 'formal', '2': 'casual', '3': 'friendly', '': 'friendly'}
    tone = tone_map.get(tone_choice, 'friendly')

    # Collect bullet points
    print("\nEnter your bullet points (one per line).")
    print("Type 'done' when you're finished:")
    print()

    bullet_points = []
    while True:
        point = input("• ").strip()
        if point.lower() == 'done':
            break
        if point:  # Only add non-empty points
            bullet_points.append(point)

    # Optional PS section
    ps = input("\nAdd a PS? (press Enter to skip): ").strip()

    # Get sender's name
    sender_name = input("Your name for the sign-off (default: Andrew): ").strip()
    if not sender_name:
        sender_name = "Andrew"

    # Generate the email
    email = generate_email(recipient_name, subject, bullet_points, tone, ps, sender_name)

    # Save to file
    with open('draft_email.txt', 'w') as f:
        f.write(email)

    # Display the email
    print("\n" + "=" * 50)
    print("✅ Your email is ready!")
    print("=" * 50)
    print()
    print(email)
    print()
    print("=" * 50)
    print("📁 Saved to: draft_email.txt")
    print("=" * 50)


def generate_email(recipient_name, subject, bullet_points, tone='friendly', ps='', sender_name='Andrew'):
    """Generate a professional email from the provided information with customizable tone"""

    # Greeting based on tone
    if tone == 'formal':
        greeting = f"Dear {recipient_name},"
        opening = "\n\nI hope this message finds you well."
        body_intro = "\n\nI am writing to inform you of the following:"
        closing = "\n\nShould you require any further information or clarification, please do not hesitate to contact me."
        sign_off_text = "Sincerely,"
    elif tone == 'casual':
        greeting = f"Hey {recipient_name},"
        opening = "\n\nHope you're doing well!"
        body_intro = "\n\nJust wanted to give you a quick update on a few things:\n"
        closing = "\n\nLet me know if you have any questions or want to chat about any of this!"
        sign_off_text = "Cheers,"
    else:  # friendly (default)
        greeting = f"Hi {recipient_name},"
        opening = "\n\nI hope this email finds you well!"
        body_intro = "\n\nI wanted to reach out to you about the following:\n"
        closing = "\n\nPlease let me know if you have any questions or need any additional information. I'm happy to help!"
        sign_off_text = "Kind Regards,"

    # Body - convert bullet points
    body = body_intro
    for point in bullet_points:
        body += f"\n• {point}"

    # Sign-off
    sign_off = f"\n\n{sign_off_text}\n{sender_name}"

    # Add PS if provided
    ps_section = ""
    if ps:
        ps_section = f"\n\nP.S. {ps}"

    # Combine all parts
    email = f"Subject: {subject}\n\n{greeting}{opening}{body}{closing}{sign_off}{ps_section}"

    return email


if __name__ == "__main__":
    main()

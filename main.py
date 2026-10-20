from pyscript import document

def candidate_checker(e):
    club_members = ["Ryan Dye", "Luis Dye", "Alicante Dye", "Dye Dye", "Rye Dye", "Emperor Ryan", "Badu Dye", "Kate Velo"]
    first_name = document.querySelector("#first-name").value.strip()
    last_name = document.querySelector("#last-name").value.strip()
    full_name = f"{first_name} {last_name}"


    is_member = full_name in club_members


    messages = [
        f"Sorry {full_name}, your name is not on the list.",
        f"Hello {full_name}! You are a part of the Rye club."
    ]

    styles = [
        "mt-4 p-3 text-center alert alert-danger border-0 d-block",
        "mt-4 p-3 text-center alert alert-success border-0 d-block"
    ]

    status_index = int(is_member)


    result_message = messages[status_index]
    result_style = styles[status_index]


    result_element = document.querySelector("#result-area")
    result_element.innerText = result_message
    result_element.className = result_style

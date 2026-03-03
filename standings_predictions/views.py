from django.shortcuts import render, redirect

# Create your views here.
from .models import Team
from .models import Submission
from .models import Player

def submit_prediction(request):

    if request.method == "POST":
        name = request.POST.get("name")
        pool_a_order = request.POST.get("pool_A")
        pool_b_order = request.POST.get("pool_B")
        pool_c_order = request.POST.get("pool_C")
        pool_d_order = request.POST.get("pool_D")

        catcher_id = request.POST.get("catcher")
        first_base_id = request.POST.get("first_base")
        second_base_id = request.POST.get("second_base")
        third_base_id = request.POST.get("third_base")
        shortstop_id = request.POST.get("shortstop")
        outfield_1_id = request.POST.get("outfield_1")
        outfield_2_id = request.POST.get("outfield_2")
        outfield_3_id = request.POST.get("outfield_3")
        pitcher_id = request.POST.get("pitcher")

        Submission.objects.create(
            name=name,
            pool_A=pool_a_order,
            pool_B=pool_b_order,
            pool_C=pool_c_order,
            pool_D=pool_d_order,

            catcher=Player.objects.filter(id=catcher_id).first(),
            first_base=Player.objects.filter(id=first_base_id).first(),
            second_base=Player.objects.filter(id=second_base_id).first(),
            third_base=Player.objects.filter(id=third_base_id).first(),
            shortstop=Player.objects.filter(id=shortstop_id).first(),
            outfield_1=Player.objects.filter(id=outfield_1_id).first(),
            outfield_2=Player.objects.filter(id=outfield_2_id).first(),
            outfield_3=Player.objects.filter(id=outfield_3_id).first(),
            pitcher=Player.objects.filter(id=pitcher_id).first(),
        )

        return redirect("submit_prediction")
        # Later you will save these to the database

    teams = Team.objects.all().order_by('pool')

    pools = {
        'A': teams.filter(pool='A'),
        'B': teams.filter(pool='B'),
        'C': teams.filter(pool='C'),
        'D': teams.filter(pool='D'),
    }

    all_teams = Team.objects.all()

    positions = ["C", "1B", "2B", "3B", "SS", "OF1", "OF2", "OF3", "P"]

    players = Player.objects.select_related("team").all()

    return render(request, "submit.html", {
    "pools": pools,
    "teams_for_dropdown": all_teams,
    "positions": positions,
    "players": players,
    })


def view_submissions(request):
    submissions = Submission.objects.all().order_by('-created_at')

    selected_submission = None
    pools = None

    submission_id = request.GET.get("submission")

    if submission_id:
        selected_submission = Submission.objects.get(id=submission_id)

        def get_ranked_teams(id_string):
            ids = id_string.split(",")
            return [Team.objects.get(id=id) for id in ids]

        pools = {
            'A': get_ranked_teams(selected_submission.pool_A),
            'B': get_ranked_teams(selected_submission.pool_B),
            'C': get_ranked_teams(selected_submission.pool_C),
            'D': get_ranked_teams(selected_submission.pool_D),
        }

    positions = ["C", "1B", "2B", "3B", "SS", "OF1", "OF2", "OF3", "P"]

    return render(request, "view_submissions.html", {
        "submissions": submissions,
        "selected_submission": selected_submission,
        "pools": pools,
        "positions": positions,
    })